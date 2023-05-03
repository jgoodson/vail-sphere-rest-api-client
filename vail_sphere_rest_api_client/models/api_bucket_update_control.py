from enum import Enum


class ApiBucketUpdateControl(str, Enum):
    BUCKETOWNERENFORCED = "BucketOwnerEnforced"
    BUCKETOWNERPREFERRED = "BucketOwnerPreferred"
    OBJECTWRITER = "ObjectWriter"

    def __str__(self) -> str:
        return str(self.value)
