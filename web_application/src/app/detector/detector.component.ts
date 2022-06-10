import { DetectorService } from './../detector.service';
import { Component, OnInit } from '@angular/core';
import { SingleHistory } from './singleHistory.model';

@Component({
  selector: 'app-detector',
  templateUrl: './detector.component.html',
  styleUrls: ['./detector.component.css'],
})
export class DetectorComponent implements OnInit {
  text: string = '';
  result: string = '';
  processing = false;
  histories: SingleHistory[] = [];

  constructor(private detectorService: DetectorService) {}

  ngOnInit(): void {}

  detectLanguage() {
    if (this.text) {
      this.processing = true;

      this.detectorService.detectLanguage(this.text).subscribe((res: any) => {
        this.processing = false;
        this.result = res;
        this.histories.push({ text: this.text, result: this.result });
        this.text = '';
      });
    }
  }

  textChanging() {
    this.result = '';
  }
}
