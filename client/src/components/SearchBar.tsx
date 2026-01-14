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
                className="w-full pl-10 py-6 text-base"
            />
        </div>
    );
};

export default SearchBar;