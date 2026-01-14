# Frontend - Employee Directory

React + TypeScript frontend for searching employees.

## 📁 What's Inside

```
src/
├── pages/
│   └── Home.tsx          # Main page (search + employee list)
├── components/
│   ├── SearchBar.tsx     # Search input box
│   ├── EmployeeList.tsx  # Grid of employee cards
│   ├── EmployeeCard.tsx  # Single employee display
│   ├── ThemeToggle.tsx   # Light/dark mode button
│   └── ui/               # Buttons, inputs, etc.
├── services/
│   └── api.ts            # Talks to backend
├── hooks/
│   └── useDebounce.ts    # Delays search (performance)
└── types/
    └── index.ts          # TypeScript definitions
```

## 🧩 Components Explained

### `Home.tsx` - Main Page
- Manages search text
- Fetches data from backend
- Shows loading/error states
- Handles pagination (next/previous)

### `SearchBar.tsx` - Search Box
- Text input with magnifying glass icon
- Updates as you type

### `EmployeeList.tsx` - Grid Container
- Shows employees in a grid
- Responsive: 1 column (mobile) → 2 (tablet) → 4 (desktop)

### `EmployeeCard.tsx` - Employee Display
- Shows name, position, department, email, join date
- Nice card design with hover effect

### `ThemeToggle.tsx` - Dark Mode Button
- Switches between light/dark theme
- Saves your choice in browser

## 🚀 Quick Start

```bash
# Install everything
npm install

# Create .env file (see below)

# Start development server
npm run dev
```

Go to http://localhost:5173

### Setup .env File

Create a `.env` file:
```env
VITE_MODE=development
VITE_API_DEV_URL=http://localhost:8000/api/v1/employees
VITE_API_PROD_URL=https://your-production-api.com/api/v1/employees
```

**What this does:**
- `VITE_MODE=development` → Uses `VITE_API_DEV_URL`
- `VITE_MODE=production` → Uses `VITE_API_PROD_URL`

### Build for Production

```bash
npm run build
```

Creates a `dist/` folder you can deploy.

## 🎨 Styling

Uses **TailwindCSS** - utility classes for styling.

**Example:**
```tsx
<div className="bg-white dark:bg-gray-900 p-4 rounded-lg">
```
- `bg-white` - White background
- `dark:bg-gray-900` - Dark gray in dark mode
- `p-4` - Padding
- `rounded-lg` - Rounded corners

### Responsive Design

**Breakpoints:**
- Default: Mobile (< 768px)
- `md:` Tablet (768px+)
- `xl:` Desktop (1280px+)

**Example:**
```tsx
<div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4">
```
This creates:
- 1 column on mobile
- 2 columns on tablet  
- 4 columns on desktop

## ✏️ Making Changes

### Add a New Component

1. Create file in `src/components/MyComponent.tsx`
2. Write your component:
```tsx
export function MyComponent() {
  return <div>Hello!</div>
}
```
3. Use it:
```tsx
import { MyComponent } from './components/MyComponent';
<MyComponent />
```

### Connect to Backend

Edit `src/services/api.ts`:
```typescript
export const getEmployeeDetails = async (id: number) => {
  const response = await axios.get(`${API_URL}/${id}`);
  return response.data;
}
```

### Add UI Component (from shadcn)

```bash
npx shadcn@latest add select
```

Then use:
```tsx
import { Select } from '@/components/ui/select';
```

## ❓ Common Issues

**Backend not connecting:**
- Make sure backend is running on port 8000
- Check `.env` file has correct API URL

**Port 5173 already in use:**
Edit `vite.config.ts`, add:
```typescript
server: { port: 3000 }
```

**TypeScript errors:**
```bash
npm run type-check
```

## 📦 What's Installed

- **React 18** - UI library
- **TypeScript** - Type safety
- **Vite** - Fast build tool
- **TailwindCSS** - Styling
- **Axios** - API calls
- **shadcn/ui** - UI components

## 📖 Learn More

- React: https://react.dev
- TypeScript: https://www.typescriptlang.org/
- TailwindCSS: https://tailwindcss.com
- shadcn/ui: https://ui.shadcn.com

---

**Need help?** Check the main README or search online!

import reactDom from 'eslint-plugin-react-dom'

export default defineConfig([
  globalIgnores(['dist']),
  {
    files: ['**/*.{ts,tsx}'],
    extends: [
      // Other configs...
      // Enable lint rules for React
      reactX.configs['recommended-typescript'],
      // Enable lint rules for React DOM
      reactDom.configs.recommended,
    ],
    languageOptions: {
      parserOptions: {
        project: ['./tsconfig.node.json', './tsconfig.app.json'],
        tsconfigRootDir: import.meta.dirname,
      },
      // other options...
    },
  },
])
```
