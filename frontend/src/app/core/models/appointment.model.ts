// Define el estado posible del turno
export type AppointmentStatus = 'PENDING' | 'CONFIRMED' | 'CANCELLED';

export interface Appointment {
    id?: number; // Opcional porque al crear uno nuevo no tiene ID
    user?: number; // ID del profesional
    professional_name?: string; // Campo extra que agregamos en el Serializer de Django

    customer_name: string;
    customer_phone: string;
    date_time: string; // Django envía fecha en formato ISO String

    status: AppointmentStatus;
    notes?: string;
    whatsapp_sent?: boolean;
    created_at?: string;
}