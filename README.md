A powerful, production-ready LinkedIn-inspired web application built with modern technologies including MongoDB, JWT authentication, Stripe payments, and Tailwind CSS. This project demonstrates advanced web development skills in building a feature-rich social platform with seamless user experience and real-world scalability.

###🔧 Features:

1.Full Authentication System with JWT and role-based access

2.MongoDB Database Integration for secure and efficient data management

3.Stripe Payment Gateway integration for premium features

4.Dynamic User Profiles with image uploads, edits, and updates

5.Social Networking Features: Connect, send/accept/reject requests

6.Content Creation Tools: Post updates, upload images, like/comment on posts

7.Personalized Feed Algorithm with suggested users and trending posts

8.Real-Time Notifications via welcome emails and user interactions

9.Modern UI/UX using Tailwind CSS and DaisyUI for responsiveness and aesthetics

###🛠️ Tech Stack:

1.Frontend: React, Tailwind CSS, DaisyUI

2.Backend: Node.js, Express.js

3.Database: MongoDB (Mongoose)

4.Authentication: JWT

5.Cloud Services: Cloudinary for image handling

6.Email Services: Mailtrap integration for transactional emails

7.Payments: Stripe API for premium features


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
