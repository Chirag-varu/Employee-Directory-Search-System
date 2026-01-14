import React from 'react';
import { Input } from './ui/input';
import { Search } from 'lucide-react';

interface SearchBarProps {
    onSearchChange: (query: string) => void;
    value: string;
}

const SearchBar: React.FC<SearchBarProps> = ({ onSearchChange, value }) => {
    const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        onSearchChange(event.target.value);
    };

    return (
        <div className="relative w-full">
            <Search className="absolute left-3 top-1/2 -translate-y-1/2 h-5 w-5 text-muted-foreground" />
            <Input
                type="text"
                placeholder="Search by name or department..."
                value={value}
                onChange={handleChange}
                className="w-full pl-10 py-5 sm:py-6 text-sm sm:text-base  dark:bg-slate-900 text-slate-900 dark:text-slate-100 border-slate-200 dark:border-slate-700 placeholder:text-slate-500 dark:placeholder:text-slate-400 focus-visible:ring-2 focus-visible:ring-primary focus-visible:ring-offset-0 dark:focus-visible:ring-slate-400 transition-all shadow-sm"
            />
        </div>
    );
};

export default SearchBar;