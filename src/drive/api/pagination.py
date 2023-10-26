from rest_framework import pagination
from rest_framework.response import Response


class LimitOffsetPagination(pagination.LimitOffsetPagination):
    def get_paginated_response(self, data):
        return Response(
            {
                "limit": self.limit,
                "offset": self.offset,
                "count": self.count,
                "results": data,
            }
        )

    def get_paginated_response_schema(self, schema):
        return {
            "type": "object",
            "properties": {
                "count": {
                    "type": "integer",
                    "example": 123,
                },
                "limit": {
                    "type": "integer",
                    "example": "100",
                },
                "offset": {
                    "type": "integer",
                    "example": "10",
                },
                "results": schema,
            },
        }
