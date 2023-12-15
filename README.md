# Social-media-API

## Description:
Social media API is RESTful API for a social media platform. The API allows users to create profiles, follow other users, create and retrieve posts, manage likes and comments, and perform basic social media actions.

## Requirements:

### User Registration and Authentication:
- Users can register with their email and password to create an account.
- Users can login with their credentials and receive a token for authentication.
- Users can logout and invalidate their token.

### User Profile:
- Users can create and update their profile, including profile picture, bio, and other details.
- Users can retrieve their own profile and view profiles of other users.
- Users can search for users by username or other criteria.

### Follow/Unfollow:
- Users can follow and unfollow other users.
- Users can view the list of users they are following and the list of users following them.

### Post Creation and Retrieval:
- Users can create new posts with text content and optional media attachments (e.g., images).
- Users can retrieve their own posts and posts of users they are following.
- Users can retrieve posts by hashtags or other criteria.

### Likes and Comments:
- Users can like and unlike posts.
- Users can view the list of posts they have liked.
- Users can add comments to posts and view comments on posts.

### Schedule Post creation using Celery:
- Added possibility to schedule Post creation.

### API Permissions:
- Only authenticated users should be able to perform actions such as creating posts, liking posts, and following/unfollowing users.
- Users can update and delete their own posts and comments.
- Users can update and delete their own profile.

### API Documentation:
- Documentation is located at /api/doc/swagger/

## Technical Requirements:
- Used Django and Django REST framework to build the API.
- Used token-based authentication for user authentication.
- Used appropriate serializers for data validation and representation.
- Used appropriate views and viewsets for handling CRUD operations on models.
- Used appropriate URL routing for different API endpoints.
- Used appropriate permissions and authentication classes to implement API permissions.
- Followed best practices for RESTful API design and documentation.

## Installation:
- git clone https://github.com/VasylTurok/social_media_api.git
- cd social_media_API
- python3 -m venv venv
- source venv/bin/activate
- pip install -r requirements.txt
- python manage.py migrate
- python manage.py runserver
