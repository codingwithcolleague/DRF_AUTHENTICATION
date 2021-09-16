from rest_framework.throttling import UserRateThrottle

class RajRateThrottle(UserRateThrottle):
    scope = 'raj'