"""
MIT License

Copyright (c) 2022 PaxxPatriot

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from typing import Any, Dict, List, Tuple

__all__ = (
    "SkinportException",
    "ClientException",
    "HTTPException",
    "ParamRequired",
    "ValidationError",
    "InvalidRequest",
    "AuthenticationError",
    "InsufficientFunds",
    "InvalidScope",
    "NotFound",
    "InternalServerError",
)


class SkinportException(Exception):
    """Base exception class for skinport.py

    Ideally speaking, this could be caught to handle any exceptions raised from this library.
    """

    pass


class ClientException(SkinportException):
    """Exception that's raised when an operation in the :class:`Client` fails.

    These are usually for exceptions that happened due to user input.
    """

    pass


class HTTPException(SkinportException):
    """Exception that's raised when an HTTP request operation fails.
    Attributes
    ------------
    response: :class:`aiohttp.ClientResponse`
        The response of the failed HTTP request. This is an
        instance of :class:`aiohttp.ClientResponse`. In some cases
        this could also be a :class:`requests.Response`.
    text: :class:`str`
        The text of the error. Could be an empty string.
    status: :class:`int`
        The status code of the HTTP request.
    """

    def __init__(self, response, message):
        self.response = response
        self.status = response.status
        if isinstance(message, dict):
            base = message.get("message", "")
            errors = message.get("errors")
            if errors:
                errors = {error["id"]: error["message"] for error in errors}
                helpful = "\n".join("In %s: %s" % t for t in errors.items())
                self.text = base + "\n" + helpful
            else:
                self.text = base
        else:
            self.text = message or ""

        fmt = "{0.status} {0.reason})"
        if len(self.text):
            fmt += ": {1}"

        super().__init__(fmt.format(self.response, self.text))


class ParamRequired(ClientException):
    """Exception that’s raised when a required parameter is not passed."""

    pass


class ValidationError(ClientException):
    """Exception that’s raised when validation of the passed parameters failed."""

    pass


class InvalidRequest(ClientException):
    """Exception that’s raised when the request couldn't be validated."""

    pass


class AuthenticationError(HTTPException):
    """Exception that’s raised for when status code 401 occurs.

    Subclass of :exc:`HTTPException`"""

    pass


class InsufficientFunds(HTTPException):
    """Exception that’s raised for when status code 402 occurs.

    Subclass of :exc:`HTTPException`"""

    pass


class InvalidScope(HTTPException):
    """Exception that’s raised for when status code 403 occurs.

    Subclass of :exc:`HTTPException`"""

    pass


class NotFound(HTTPException):
    """Exception that’s raised for when status code 404 occurs.

    Subclass of :exc:`HTTPException`"""

    pass


class InternalServerError(HTTPException):
    """Exception that’s raised for when a 500 range status code occurs.

    Subclass of :exc:`HTTPException`"""

    pass
