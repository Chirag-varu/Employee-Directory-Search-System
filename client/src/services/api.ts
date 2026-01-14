import axios from 'axios';

const API_URL = 'http://localhost:8000/api/employees';

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