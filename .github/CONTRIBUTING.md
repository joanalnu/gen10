# Contributing
Thank you for your interest in contributing to this project! To align with our community standards, you can contribute by creating an [issue](#steps-for-creating-good-issues) or submitting a [pull request](#steps-for-creating-good-pull-requests). Follow the steps below to ensure a smooth contribution process.

## Steps for Creating Good Issues

1. Identify a bug or a feature you'd like to see.
2. Check the [Issues page](https://github.com/joanalnu/gen_api/issues/) to ensure the issue hasn't already been reported.
3. If not, click the green "New Issue" button in the upper-right corner.
4. Choose an appropriate template (if available) or create a blank issue.
5. Clearly describe the bug or feature, following the instructions in the chosen template.

## Steps for creating good pull requests
1. Identify a bug or a feature you're missing.
2. Fork the repository, then clone it into your machine by running
  ```bash
  git clone https://github.com/your-user-name/gen_api.git
  ```
3. Access the repository (```cd gen_api```) and create a new branch:
  ```bash
  git checkout -b <your-name>/<new-feature>
  ```
4. Install the requirements. Consider creating a new conda environment to avoid problems with libraries and versions.
  ```bash
  pip install -r requirements.txt
  ```
5. Make sure the testing pass on your machine by running `pytest`.
6. Develop your code and run the integrated testing (see point 6) and add new testing if needed.
7. Once you have finished and passed all tests, stage, commit, and push to your fork:
  ```bash
  git add .
  git commit -m "Brief description of your changes"
  git push origin <name>/<new_feature>
  ```
8. Open the repository in the browser and create and submit a pull request. Describe you changes in a clear comment.
9. The pull request will be reviewed and tested by the owners of the repository and approved or closed with feedback.

Remember this good practices:
- Follow the standards for style and code quality.
- Write additional tests.
- Keep your changes focues. Create separate pull requests if different changes are not dependent of each other.
- Write good commit messages.

## Link to code of conduct
By contributing either way to this project you agree to abide to the terms of our [Code of Conduct](https://github.com/joanalnu/gen_api/CODE_OF_CONDUCT.md).

## Contact
Feel free to [contact me](https://joanalnu.github.io/contact).
