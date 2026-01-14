import React, { useEffect, useState, useCallback } from 'react';
import SearchBar from '../components/SearchBar';
import EmployeeList from '../components/EmployeeList';
import { fetchEmployees } from '../services/api';
import type { Employee } from '../types/index';
import { useDebounce } from '../hooks/useDebounce';
import { Alert, AlertDescription, AlertTitle } from '@/components/ui/alert';
import { Button } from '@/components/ui/button';
import { Loader2, ServerCrash, UserX, ChevronLeft, ChevronRight } from 'lucide-react';

const ITEMS_PER_PAGE = 8;

const Home: React.FC = () => {
    const [employees, setEmployees] = useState<Employee[]>([]);
    const [loading, setLoading] = useState<boolean>(true);
    const [error, setError] = useState<string | null>(null);
    const [searchTerm, setSearchTerm] = useState('');
    const [currentPage, setCurrentPage] = useState(1);

    const debouncedSearchTerm = useDebounce(searchTerm, 500);

    const loadEmployees = useCallback(async (search: string, page: number) => {
        setLoading(true);
        setError(null);
        try {
            const offset = (page - 1) * ITEMS_PER_PAGE;
            const data = await fetchEmployees(search, ITEMS_PER_PAGE, offset);
            setEmployees(data);
        } catch (err) {
            setError('Failed to fetch employees. Is the backend server running?');
        } finally {
            setLoading(false);
        }
    }, []);

    useEffect(() => {
        setCurrentPage(1); // Reset to page 1 when search term changes
    }, [debouncedSearchTerm]);

    useEffect(() => {
        loadEmployees(debouncedSearchTerm, currentPage);
    }, [debouncedSearchTerm, currentPage, loadEmployees]);

    const handlePreviousPage = () => {
        if (currentPage > 1) {
            setCurrentPage(prev => prev - 1);
        }
    };

    const handleNextPage = () => {
        if (employees.length === ITEMS_PER_PAGE) {
            setCurrentPage(prev => prev + 1);
        }
    };

    const clearFilters = () => {
        setSearchTerm('');
        setCurrentPage(1);
    };

    const renderContent = () => {
        if (loading) {
            return (
                <div className="flex flex-col items-center justify-center gap-4 text-muted-foreground">
                    <Loader2 className="h-12 w-12 animate-spin" />
                    <p className="text-lg">Loading Employees...</p>
                </div>
            );
        }

        if (error) {
            return (
                <Alert variant="destructive" className="max-w-lg mx-auto">
                    <ServerCrash className="h-4 w-4" />
                    <AlertTitle>Error</AlertTitle>
                    <AlertDescription>{error}</AlertDescription>
                </Alert>
            );
        }

        if (employees.length === 0) {
            return (
                <div className="flex min-h-100 flex-col items-center justify-center rounded-xl border-2 border-dashed border-muted/50 bg-muted/5 p-8 text-center animate-in fade-in zoom-in duration-300">
                    {/* Icon Container with subtle glow */}
                    <div className="relative mb-4 flex h-20 w-20 items-center justify-center rounded-full bg-muted/10">
                        <UserX className="h-10 w-10 text-muted-foreground/60" />
                        <div className="absolute inset-0 rounded-full bg-primary/5 blur-xl" />
                    </div>

                    {/* Text Content */}
                    <h3 className="text-xl font-semibold tracking-tight text-foreground">
                        No employees found
                    </h3>
                    <p className="mt-2 max-w-62.5 text-sm text-muted-foreground">
                        We couldn't find anyone matching <span className="font-medium text-foreground italic">"{searchTerm}"</span>. Try adjusting your search or department filters.
                    </p>

                    {/* Action Button (Optional but recommended) */}
                    <button
                        onClick={clearFilters}
                        className="mt-6 text-sm font-medium text-primary hover:underline underline-offset-4"
                    >
                        Clear all filters
                    </button>
                </div>
            );
        }

        return <EmployeeList employees={employees} />;
    };

    return (
        <div className="container mx-auto p-4 sm:p-6 md:p-8">
            <header className="text-center mb-10">
                <h1 className="text-4xl sm:text-5xl font-bold tracking-tight">Employee Directory</h1>
                <p className="text-muted-foreground mt-2">The right people, right away.</p>
            </header>

            <div className="max-w-2xl mx-auto mb-10">
                <SearchBar onSearchChange={setSearchTerm} value={searchTerm} />
            </div>

            <main className="min-h-100">
                {renderContent()}

                {/* Pagination Controls */}
                {!loading && !error && employees.length > 0 && (
                    <div className="flex items-center justify-center gap-4 mt-8">
                        <Button
                            variant="outline"
                            onClick={handlePreviousPage}
                            disabled={currentPage === 1}
                            className="flex items-center gap-2"
                        >
                            <ChevronLeft className="h-4 w-4" />
                            Previous
                        </Button>

                        <span className="text-sm text-muted-foreground">
                            Page {currentPage}
                        </span>

                        <Button
                            variant="outline"
                            onClick={handleNextPage}
                            disabled={employees.length < ITEMS_PER_PAGE}
                            className="flex items-center gap-2"
                        >
                            Next
                            <ChevronRight className="h-4 w-4" />
                        </Button>
                    </div>
                )}
            </main>
        </div>
    );
};

export default Home;