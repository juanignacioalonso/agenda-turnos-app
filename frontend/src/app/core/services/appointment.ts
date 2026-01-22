import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Appointment } from '../models/appointment.model';

@Injectable({
  providedIn: 'root' // Esto hace que el servicio esté disponible en toda la app
})
export class AppointmentService {
  // URL de tu Backend Django
  private apiUrl = 'http://127.0.0.1:8000/api/appointments/';

  constructor(private http: HttpClient) { }

  // 1. Obtener todos los turnos
  getAll(): Observable<Appointment[]> {
    return this.http.get<Appointment[]>(this.apiUrl);
  }

  // 2. Crear un turno
  create(appointment: Appointment): Observable<Appointment> {
    return this.http.post<Appointment>(this.apiUrl, appointment);
  }

  // 3. Eliminar un turno
  delete(id: number): Observable<void> {
    return this.http.delete<void>(`${this.apiUrl}${id}/`);
  }

  // 4. Actualizar un turno
  update(id: number, data: Partial<Appointment>): Observable<Appointment> {
    return this.http.patch<Appointment>(`${this.apiUrl}${id}/`, data);
  }
}