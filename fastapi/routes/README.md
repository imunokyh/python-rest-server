# Authorization
### Bearer Token
- bearer 값과 token 을 포함
    - token 은 expiration 존재
    - token 이 유통기한이 지나면 다시 로그인 필요
### JWT (JSON Web Token)
- standard to codify a JSON object ([jwt](https://jwt.io/))
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```
- need to install some package
    - **python-jose[cryptography]** *// generate and verify the JWT tokens*
    - **passlib[bcrypt]** *// handle password hashes*