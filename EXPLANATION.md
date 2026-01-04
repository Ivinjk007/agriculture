
# Project Explanation (Hackathon Ready)

## Objective
To build a lightweight, real-time animal intrusion detection system for crop protection using computer vision.

## System Flow
Camera → Frame Preprocessing → YOLO Inference → Confidence Filtering → Alert Trigger → Cooldown → Resume Monitoring

## Why YOLOv8 Nano?
- Optimized for CPU usage
- Fast inference on laptops
- Suitable for 24-hour hackathon constraints

## CPU Optimization Techniques
- Frame resizing (640x640)
- Confidence thresholding
- Cooldown-based alert system
- Can be extended to frame skipping & ROI

## Hackathon Scope
This system acts as an early warning mechanism and is not a replacement for physical fencing or manual monitoring.
