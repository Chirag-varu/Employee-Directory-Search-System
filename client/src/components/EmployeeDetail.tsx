import React from 'react';
import { useParams } from 'react-router-dom';
import { fetchEmployeeById } from '../services/api';
import type { Employee } from '../types';

const EmployeeDetail: React.FC = () => {
    const { id } = useParams<{ id: string }>();
    const [employee, setEmployee] = React.useState<Employee | null>(null);
    const [loading, setLoading] = React.useState(true);
    const [error, setError] = React.useState<string | null>(null);

    React.useEffect(() => {
        const fetchEmployeeDetail = async () => {
            try {
                const data = await fetchEmployeeById(id);
                console.log('====================================');
                console.log(data);
                console.log('====================================');
                setEmployee(data);
            } catch (err: any) {
                setError('Failed to fetch employee details');
            } finally {
                setLoading(false);
            }
        };

        fetchEmployeeDetail();
    }, [id]);

    if (loading) {
        return <div>Loading...</div>;
    }

    if (error) {
        return <div>Error: {error}</div>;
    }

    if (!employee) {
        return <div>No employee found</div>;
    }

    return (
        <div>
            <h2>{employee.name}</h2>
            <p>Email: {employee.email}</p>
            <p>Department: {employee.department}</p>
            <p>Designation: {employee.designation}</p>
            <p>Date of Joining: {employee.date_of_joining}</p>
        </div>
    );
};

export default EmployeeDetail;