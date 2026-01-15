import React, { useEffect, useState, useCallback } from 'react';
import SearchBar from '../components/SearchBar';
import EmployeeList from '../components/EmployeeList';
import { ThemeToggle } from '../components/ThemeToggle';
import { fetchEmployees } from '../services/api';
// import type { Employee } from '../types/index';
import { useDebounce } from '../hooks/useDebounce';
import { Alert, AlertDescription, AlertTitle } from '@/components/ui/alert';
import { Button } from '@/components/ui/button';
import { Loader2, ServerCrash, UserX, ChevronLeft, ChevronRight } from 'lucide-react';

const ITEMS_PER_PAGE = Number(import.meta.env.VITE_ITEMS_PER_PAGE) || 8;

const Home: React.FC = () => {
    const [employees, setEmployees] = useState<any[]>([]);
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
            console.log('=234===================================');
            console.log(data);
            console.log('==12412==================================');
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
            const isOnlySpaces = searchTerm.trim() === '' && searchTerm.length > 0;
            
            return (
                <div className="flex min-h-100 flex-col items-center justify-center rounded-xl border-2 border-dashed border-muted/50 bg-muted/5 p-8 text-center animate-in fade-in zoom-in duration-300">
                    {/* Icon Container with subtle glow */}
                    <div className="relative mb-4 flex h-20 w-20 items-center justify-center rounded-full bg-muted/10">
                        <UserX className="h-10 w-10 text-muted-foreground/60" />
                        <div className="absolute inset-0 rounded-full bg-primary/5 blur-xl" />
                    </div>

                    {/* Text Content */}
                    <h3 className="text-xl font-semibold tracking-tight text-foreground">
                        {isOnlySpaces ? 'Invalid search' : 'No employees found'}
                    </h3>
                    <p className="mt-2 max-w-62.5 text-sm text-muted-foreground">
                        {isOnlySpaces 
                            ? 'Please enter a valid search term. Spaces alone are not a valid search.'
                            : <>We couldn't find anyone matching <span className="font-medium text-foreground italic">"{searchTerm}"</span>. Try adjusting your search or department filters.</>
                        }
                    </p>

                    {/* Action Button (Optional but recommended) */}
                    <Button
                        onClick={clearFilters}
                        className="mt-6 px-4 py-2 bg-slate-100 hover:bg-slate-200 text-slate-700 text-sm font-medium rounded-lg transition-all"
                    >
                        Clear all filters
                    </Button>
                </div>
            );
        }

        return <EmployeeList employees={employees} />;
    };

    return (
        <div className="container mx-auto px-4 py-6 sm:px-6 sm:py-8 md:px-8 md:py-10">
            <div className="fixed top-4 right-4 z-50 sm:absolute">
                <ThemeToggle />
            </div>

            <header className="text-center mb-8 sm:mb-10 mt-2">
                <h1 className="text-3xl sm:text-4xl md:text-5xl font-bold tracking-tight">Employee Directory</h1>
                <p className="text-sm sm:text-base text-muted-foreground mt-2">The right people, right away.</p>
            </header>

            <div className="max-w-2xl mx-auto mb-8 sm:mb-10 px-2 sm:px-0">
                <SearchBar onSearchChange={setSearchTerm} value={searchTerm} />
            </div>

            <main className="min-h-100">
                {renderContent()}

                {/* Pagination Controls */}
                {!loading && !error && employees.length > 0 && (
                    <div className="flex flex-wrap items-center justify-center gap-3 sm:gap-4 mt-6 sm:mt-8">
                        <Button
                            variant="outline"
                            onClick={handlePreviousPage}
                            disabled={currentPage === 1}
                            className="flex items-center gap-1 sm:gap-2 text-sm"
                            size="sm"
                        >
                            <ChevronLeft className="h-4 w-4" />
                            <span className="hidden xs:inline">Previous</span>
                            <span className="xs:hidden">Prev</span>
                        </Button>

                        <span className="text-xs sm:text-sm text-muted-foreground px-2">
                            Page {currentPage}
                        </span>

                        <Button
                            variant="outline"
                            onClick={handleNextPage}
                            disabled={employees.length < ITEMS_PER_PAGE}
                            className="flex items-center gap-1 sm:gap-2 text-sm"
                            size="sm"
                        >
                            <span className="hidden xs:inline">Next</span>
                            <span className="xs:hidden">Next</span>
                            <ChevronRight className="h-4 w-4" />
                        </Button>
                    </div>
                )}
            </main>
        </div>
    );
};

export default Home;