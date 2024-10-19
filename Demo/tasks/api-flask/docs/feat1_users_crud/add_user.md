# Test Cases for Create User

| Test Case ID | Description | Input | Expected Output |
|--------------|-------------|-------|-----------------|
| TC01         | Validate email uniqueness | Email: existing@example.com | Error: "Email already exists" |
| TC02         | Validate email format | Email: invalid-email | Error: "Invalid email format" |
| TC03         | Validate phone length | Phone: 123456789 | Error: "Phone number must be 10 digits" |
| TC04         | Validate password length | Password: short | Error: "Password must be longer than 6 characters" |
| TC05         | Successful user creation | Email: new@example.com, Phone: 1234567890, Password: strongpassword | Success: "User created successfully" |
