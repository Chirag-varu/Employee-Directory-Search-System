import { Moon, Sun } from 'lucide-react';
import { Toggle } from './ui/toggle';
import { useTheme } from './ThemeProvider';

export function ThemeToggle() {
    const { theme, setTheme } = useTheme();

    return (
        <Toggle
            pressed={theme === 'dark'}
            onPressedChange={(pressed) => setTheme(pressed ? 'dark' : 'light')}
            aria-label="Toggle theme"
            className="rounded-full"
        >
            <Sun className="h-[1.2rem] w-[1.2rem] rotate-0 scale-100 transition-all dark:-rotate-90 dark:scale-0" />
            <Moon className="absolute h-[1.2rem] w-[1.2rem] rotate-90 scale-0 transition-all dark:rotate-0 dark:scale-100" />
        </Toggle>
    );
}
