from pydantic import BaseModel, EmailStr, Field


# ~~~~~~~~~~~~~~~~~~~~~ OAuth1 Schemas ~~~~~~~~~~~~~~~~~~~~~ #

class SignUp(BaseModel):
    username: str = Field(title='username', description='user username', examples=['allelleo'])
    first_name: str = Field(title='first name', description='user first name', examples=['Alexey'])
    last_name: str = Field(title='last name', description='user last name', examples=['Ovchinnikov'])
    email: EmailStr = Field(title='email', description='user email', examples=['user@example.com'])
    password: str


class SignUpOutput(BaseModel):
    token: str


class SignIn(BaseModel):
    email: EmailStr
    password: str


SignInOutput = SignUpOutput
# ~~~~~~~~~~~~~~~~~~~~~ OAuth1 Schemas ~~~~~~~~~~~~~~~~~~~~~ #
