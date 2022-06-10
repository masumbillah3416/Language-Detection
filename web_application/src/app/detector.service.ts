import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root',
})
export class DetectorService {
  constructor(private http: HttpClient) {}

  detectLanguage(text: string) {
    return this.http.get(
      `https://detectlanguage.herokuapp.com/api/check-language/?text=${text}`,
      {
        responseType: 'text',
      }
    );
  }
}
