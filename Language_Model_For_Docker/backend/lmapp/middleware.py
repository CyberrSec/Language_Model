from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response

class CSPMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, policy: str):
        super().__init__(app)
        self.policy = policy

    async def dispatch(self, request, call_next):
        response: Response = await call_next(request)
        response.headers['Content-Security-Policy'] = self.policy
        return response
