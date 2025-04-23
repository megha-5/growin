A powerful, production-ready LinkedIn-inspired web application built with modern technologies including MongoDB, JWT authentication, Stripe payments, and Tailwind CSS. This project demonstrates advanced web development skills in building a feature-rich social platform with seamless user experience and real-world scalability.

###🔧 Features:
Full Authentication System with JWT and role-based access

MongoDB Database Integration for secure and efficient data management

Stripe Payment Gateway integration for premium features

Dynamic User Profiles with image uploads, edits, and updates

Social Networking Features: Connect, send/accept/reject requests

Content Creation Tools: Post updates, upload images, like/comment on posts

Personalized Feed Algorithm with suggested users and trending posts

Real-Time Notifications via welcome emails and user interactions

Modern UI/UX using Tailwind CSS and DaisyUI for responsiveness and aesthetics

###🛠️ Tech Stack:
Frontend: React, Tailwind CSS, DaisyUI

Backend: Node.js, Express.js

Database: MongoDB (Mongoose)

Authentication: JWT

Cloud Services: Cloudinary for image handling

Email Services: Mailtrap integration for transactional emails

Payments: Stripe API for premium features


### Setup .env file

```bash
PORT=5000
MONGO_URI=<your_mongo_uri>

JWT_SECRET=<yourverystrongsecret>

NODE_ENV=development

MAILTRAP_TOKEN=<your_mailtrap_token>
EMAIL_FROM=mailtrap@demomailtrap.com
EMAIL_FROM_NAME=<Your_Name>

CLOUDINARY_API_KEY=<your_cloudinary_api_key>
CLOUDINARY_API_SECRET=<your_cloudinary_api_secret>
CLOUDINARY_CLOUD_NAME=<your_cloudinary_cloud_name>

CLIENT_URL=http://localhost:5173
```

### Run this app locally

```shell
npm run build
```

### Start the app

```shell
npm run start
```
