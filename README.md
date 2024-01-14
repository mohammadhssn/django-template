### TODO:

1. Rename the .env.sample file to .env:
   #### ` mv .env.sample .env `
2. Build Docker containers using the development configuration:
   #### ` docker-compose -f docker-compose.dev.yml build `

3. Start the Docker containers with the development configuration:
   #### ` docker-compose -f docker-compose.dev.yml up `

4. Install pre-commit hooks:
   #### ` make install-pre-commit `

5. Run linting checks:
   #### ` make lint `

6. Migrations:
   #### ` make migrations `
   #### ` make migrate `

7. Start the server:
   #### ` make run-server `
