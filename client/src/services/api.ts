import axios from 'axios';

const MODE = import.meta.env.VITE_MODE || 'development';
const API_URL = MODE === 'production' 
    ? import.meta.env.VITE_API_PROD_URL 
    : import.meta.env.VITE_API_DEV_URL;

export const fetchEmployees = async (query: string, limit: number = 8, offset: number = 0) => {
    try {
        const response = await axios.get(API_URL, {
            params: { 
                search: query,
                limit: limit,
                offset: offset
            }
        });
        return response.data;
    } catch (error) {
        console.error('Error fetching employees:', error);
        throw error;
    }
};

export const fetchEmployeeById = async (id?: string) => {
    try {
        const response = await axios.get(`${API_URL}/${id}`);
        return response.data;
    } catch (error) {
        console.error('Error fetching employee by ID:', error);
        throw error;
    }
};