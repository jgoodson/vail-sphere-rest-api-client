from enum import Enum


class ApiBucketCommonControl(str, Enum):
    BUCKETOWNERENFORCED = "BucketOwnerEnforced"
    BUCKETOWNERPREFERRED = "BucketOwnerPreferred"
    OBJECTWRITER = "ObjectWriter"

    def __str__(self) -> str:
        return str(self.value)
