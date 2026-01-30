import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import {ContainerComponent} from "../container/container.component";
import {MatIconModule} from '@angular/material/icon';

@Component({
  selector: 'app-contact',
  standalone: true,
  imports: [CommonModule, ContainerComponent, MatIconModule],
  templateUrl: './contact.component.html',
  styleUrls: ['./contact.component.scss']
})
export class ContactComponent { }
