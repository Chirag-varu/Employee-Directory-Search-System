import React from 'react';
import { Card, CardContent, CardHeader, CardTitle } from './ui/card';
import type { Employee } from '../types/index';
import { Briefcase, Mail, Calendar } from 'lucide-react';

interface EmployeeCardProps {
    employee: Employee;
}

export const EmployeeCard: React.FC<EmployeeCardProps> = ({ employee }) => {
    return (
        <Card className="bg-card/50 backdrop-blur-sm border-border/20 hover:border-primary/50 transition-all duration-300 transform hover:-translate-y-1 hover:shadow-lg cursor-pointer">
            <CardHeader className="pb-3">
                <CardTitle className="text-lg sm:text-xl font-bold text-primary-foreground">{employee.name}</CardTitle>
                <p className="text-xs sm:text-sm text-muted-foreground font-medium">{employee.designation}</p>
            </CardHeader>
            <CardContent className="space-y-2 sm:space-y-3 text-xs sm:text-sm">
                <div className="flex items-center gap-2 sm:gap-3">
                    <Briefcase className="h-3.5 w-3.5 sm:h-4 sm:w-4 text-muted-foreground flex-shrink-0" />
                    <span className="truncate">{employee.department}</span>
                </div>
                <div className="flex items-center gap-2 sm:gap-3">
                    <Mail className="h-3.5 w-3.5 sm:h-4 sm:w-4 text-muted-foreground flex-shrink-0" />
                    <a href={`mailto:${employee.email}`} className="hover:text-primary transition-colors truncate">
                        {employee.email}
                    </a>
                </div>
                <div className="flex items-center gap-2 sm:gap-3">
                    <Calendar className="h-3.5 w-3.5 sm:h-4 sm:w-4 text-muted-foreground flex-shrink-0" />
                    <span className="truncate">Joined: {new Date(employee.date_of_joining).toLocaleDateString()}</span>
                </div>
            </CardContent>
        </Card>
    );
};

export default EmployeeCard;