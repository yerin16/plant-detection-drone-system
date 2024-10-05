# Development of an AI-based Drone System for Surveillance and Management of Invasive Plants in Jeju Island, South Korea

This project focuses on the development of a drone-based system that detects and manages invasive alien plants (IVPs), particularly Ambrosia trifida, in Jeju Island, South Korea. The system uses a YOLOv5 object detection model integrated with drone systems for real-time detection and removal of IVPs in hard-to-access regions like Jeju Island in South Korea.
![Plant Detection](https://github.com/yerin16/plant-detection-drone-system/blob/main/images/detection.png?raw=true)


## Table of Contents

- [Background](#background)
- [Features](#features)
- [Models](#models)
- [Result](#result)
- [Conclusion](#conclusion)


## Background
My homtown, Jeju Island known for its rich biodiversity and unique endemic plants, has faced increasing threats due to invasive alien plants (IVPs). These plants, such as Ambrosia trifida, have disrupted the local ecosystem, competing with native species and negatively impacting biodiversity. Given the limited manpower and the challenge of accessing remote areas of Jeju Island, an automated, scalable solution was needed to effectively monitor and manage the spread of IVPs.

In addition, Ambrosia trifida is particularly problematic due to its high reproductive capacity and resemblance to native species, making detection difficult. Current methods involving human labor are insufficient, especially in areas inaccessible to people. This project aims to automate the detection and removal of IVPs by using drones equipped with the object detection models to offer a promising alternative for efficient and accurate IVP management.
![Distribution of Ambrosia Trifida in Jeju](https://github.com/yerin16/plant-detection-drone-system/blob/main/images/jeju-distribution.png?raw=true)

## Features

- Drone-Based Image Collection: Drones collect high-resolution images of invasive plants in inaccessible regions.
- Real-Time Object Detection: Utilizes YOLOv5 for fast and accurate identification of Ambrosia trifida.
- Server-Drone Communication: A centralized system that manages the communication between detection and surveillance drones for removing IVPs.

## Models

### 1. YOLOv5 Object Detection Model
The YOLOv5 model was selected for object detection due to its efficiency in real-time tasks. The model was trained on the dataset of 1,640 labeled images, with an average precision (mAP) of 48.1%, indicating its capability to detect Ambrosia trifida in various environmental backgrounds.

### 2. Drone System
The drones used in the project were Tello Edu drones, which can be controlled programmatically. The system was developed to manage drone flights, image collection, and real-time communication between drones and the central server. Images captured by the drones are sent to the server, where they are processed by the detection model, and the surveillance drone is dispatched to remove detected plants.

## Result
The model was trained on 1,640 images with a mean average precision (mAP) of 48.1%, capable of detecting Ambrosia trifida even in complex backgrounds.
![Distribution of Ambrosia Trifida in Jeju](https://github.com/yerin16/plant-detection-drone-system/blob/main/images/map.png?raw=true)
![Distribution of Ambrosia Trifida in Jeju](https://github.com/yerin16/plant-detection-drone-system/blob/main/images/confusion-matrix.png?raw=true)

## Conclusion
This project demonstrates the feasibility of using AI-powered drones for the detection and management of invasive plants, offering a scalable solution to ecosystem management challenges in hard-to-reach regions like Jeju Island. Future improvements include expanding the dataset and enhancing drone battery life for longer missions.