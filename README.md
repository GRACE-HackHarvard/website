# GRACE - Generative Real-Time Astronomy and Celestial Experience
Exactly what it sounds like

## Inspiration

Many of us never had the privilege of genuinely seeing stars in the night sky. Given the complexity of space and the abstract nature of studying it, our team strives to bring the cosmos to the home, creating an augmented, immersive, and educational experience that can ignite lifelong interest and inspire the next generation of future scientists to change our world.

Motivated by the wizardry of Iron Man interacting with his virtual tech, we set out to use our machine learning/AI and full-stack development experiences to make this idea a reality.

## What it does

Using just a projector, a laptop, and a dark room, GRACE creates an engaging interactive star map. Participants can navigate the celestial expanse by employing a nifty laser pointer that mimics a telescope, which enables them to zoom in on specific stars and delve deeper into their characteristics.

## How we built it

Utilizing the Jinja template and Tailwind, our front end tackled the wonders of space with cozy graphics and a dark color theme with black, purple, and dark blue. Featuring modern web design including elements like animations on scroll, our frontend is simple but professional.

We used a Flask backend connected with SocketIO to effectively communicate between the JavaScript Camera input and our AI and Machine Learning models that use them, including computer vision and language transformers. We found the largest area with a significant luminosity over a certain threshold to detect our flashlight selecting stars. To make scientific knowledge accessible, we scraped abstracts from scientific literature and used the Pegasus transformer model to generate summaries.

## Challenges we ran into

One challenge was integrating the computer vision into the web app and having the backend interact with the frontend. Calibrating the camera with the projector was extremely challenging in its own right, as we have to use an additional step to transform the projected image and flashlight pointer into information on our web app. Zooming into the stars and getting a snapshot was far harder than expected. Transforming the right angle and declination of the API to the azimuthal coordinate system of the stars used quite a bit of challenging math and physics.

## Accomplishments that we're proud of

We’re really proud of undertaking this ambitious project and being able to successfully build an interactive star map that fulfilled our Tony Stark virtual tech aspirations.

## What we learned

We learned a lot more than just new computer science methods. Beyond working with computer vision and integrating it into the Flask application, we also learned a ton about astrophysics coordinate systems.

## What's next for GRACE: Generative Real-Time Astronomy & Celestial Experience

In the future, we plan to train a more robust pose estimation model, which would be better in detecting the limbs of the users. We can detect arm motions with this, and with a simple flourish of the arm, we can scroll through the night sky. We can implement more functionality such that you can push your arm outwards to zoom into the specific area of the night sky.
