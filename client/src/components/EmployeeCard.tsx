import React from 'react';
import { Card, CardContent, CardHeader, CardTitle } from './ui/card';
import type { Employee } from '../types/index';
import { Briefcase, Mail, Calendar } from 'lucide-react';

interface EmployeeCardProps {
    employee: Employee;
}

export const EmployeeCard: React.FC<EmployeeCardProps> = ({ employee }) => {
    return (
        <Card className="bg-card/50 backdrop-blur-sm border-border/20 hover:border-primary/50 transition-all duration-300 transform hover:-translate-y-1 hover:shadow-lg">
            <CardHeader>
                <CardTitle className="text-xl font-bold text-primary-foreground">{employee.name}</CardTitle>
                <p className="text-sm text-muted-foreground font-medium">{employee.designation}</p>
            </CardHeader>
            <CardContent className="space-y-3 text-sm">
                <div className="flex items-center gap-3">
                    <Briefcase className="h-4 w-4 text-muted-foreground" />
                    <span>{employee.department}</span>
                </div>
                <div className="flex items-center gap-3">
                    <Mail className="h-4 w-4 text-muted-foreground" />
                    <a href={`mailto:${employee.email}`} className="hover:text-primary transition-colors">
                        {employee.email}
                    </a>
                </div>
                <div className="flex items-center gap-3">
                    <Calendar className="h-4 w-4 text-muted-foreground" />
                    <span>Joined: {new Date(employee.date_of_joining).toLocaleDateString()}</span>
                </div>
            </CardContent>
        </Card>
    );
};

export default EmployeeCard;