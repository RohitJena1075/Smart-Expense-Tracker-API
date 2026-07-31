# AI_NOTES

# AI Usage Notes

I used ChatGPT while building this project, mainly to speed up development and to get help whenever I was unsure about an approach. I built the project step by step, reviewed every suggestion, and tested everything before keeping it.

## 1. Which parts were AI-generated and which were written by me?

I used AI to help with:

* Planning the folder structure.
* Improving FastAPI endpoints and Pydantic models.
* Writing the JSON file handling functions.
* Generating the initial pytest test cases.
* Improving the README and this AI_NOTES file.

My part was:

* Creating initial structure of FastAPI endpoints and models.
* Putting all the pieces together into a working project.
* Understanding the suggested code before using it.
* Fixing errors that came up during development.
* Making changes whenever something didn't work as expected.
* Running the API manually through Swagger to verify every endpoint.
* Running the test suite and fixing issues until all tests passed.

## 2. What did I validate, test, or change?

I validate every endpoint myself instead of assuming the generated code was correct.

I tested the following:

* Creating expenses
* Viewing all expenses
* Filtering by category
* Calculating totals
* Deleting expenses
* Invalid input cases

Made changes during development, especially around JSON storage and the test setup, so that the tests would use a temporary file instead of modifying the application's actual data. Before submitting, I verified that the server starts correctly and that all tests pass.

## 3. Any AI suggestion you decided not to use?

Yes, Some suggestions included adding a database, authentication, logging, etc. I decided not to include those because the assignment specifically mentioned using a local JSON file and only required the core expense tracking features (plus one bonus feature). I wanted to keep the project focused on the assignment requirements instead of adding unnecessary complexity.
