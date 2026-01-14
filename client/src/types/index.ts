export interface Employee {
  id: number;
  name: string;
  email: string;
  department: string;
  designation: string;
  date_of_joining: string;
}

export interface SearchParams {
  query: string;
  department?: string;
}

export interface ApiResponse<T> {
  data: T;
  message: string;
  success: boolean;
}