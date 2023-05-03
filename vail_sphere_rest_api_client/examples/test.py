from vail_sphere_rest_api_client import Client, AuthenticatedClient
from vail_sphere_rest_api_client.api.default import create_token_credential, create_bucket
from vail_sphere_rest_api_client.models import (
    ApiToken, ApiCredentials, 
    ApiBucket, PolicyDocument, PolicyDocumentStatement, 
    ServerValidationErrorResponse
    )

# Create the unauthenticated client
c = Client(
    base_url="https://10.1.128.31:8443",
    raise_on_unexpected_status=True
)

# Construct the credentials object
api_creds = ApiCredentials(
    "Administrator",
    password="NotTheRealPassword"
)

# Synchronous API call to get token
token = create_token_credential.sync(client=c, json_body=api_creds)

# Check whether token returned properly
if not isinstance(token, ApiToken):
    raise ConnectionError("Failed to authenticate to API")

# Check whether return actually has a valid token in it
if isinstance(token.token, str):
    api = AuthenticatedClient(
        "https://10.1.128.31:8443",
        token=token.token
    )
else:
    raise ConnectionError("Failed to get authentication token")

# Create a bucket with a Bucket Policy
# Policies are just JSON documents with str key/values and can do all sorts of stuff
# We create them from a Python dict, presumably with all strings.
bucket_policy = PolicyDocument(
    statement=PolicyDocumentStatement.from_dict({
        "Principal": "*",
        "Effect": "Deny", # The safest bucket - the kind no one can use
    }),
    version="0.0.1"
    )

# Create the request object from a Model. Some arguments are base types, some are Models themselves like policy
bucket_create = create_bucket.ApiBucketCreate(
    "test_bucket",
    compress=True,
    encrypt=False,
    policy=bucket_policy
    )

# Actually create the bucket. 
bucket = create_bucket.sync(client=api, json_body=bucket_create)

# More return type checking since this API likes to return ServerValidationErrorResponse objects
# We could check for those explicity if they return useful information and ever actually happen
# Probably work logging or something
if not isinstance(bucket, ApiBucket):
    raise 