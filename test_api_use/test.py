from vail_sphere_rest_api_client import Client, AuthenticatedClient
from vail_sphere_rest_api_client.api.default import create_token_credential, create_bucket
from vail_sphere_rest_api_client.models import policy_document, policy_document_statement, ApiToken, ApiCredentials, ApiBucket, ServerValidationErrorResponse

c = Client(
    base_url="https://10.1.128.31:8443",
    raise_on_unexpected_status=True
)

api_creds = ApiCredentials(
    "Administrator",
    password="NotTheRealPassword"
)

token = create_token_credential.sync(client=c, json_body=api_creds)

if not isinstance(token, ApiToken):
    raise ConnectionError("Failed to authenticate to API")

if isinstance(token.token, str):
    api = AuthenticatedClient(
        "https://10.1.128.31:8443",
        token=token.token
    )
else:
    raise ConnectionError("Failed to get authentication token")


bucket_policy = policy_document.PolicyDocument(
    statement=policy_document_statement.PolicyDocumentStatement.from_dict(
            {"statement": "I don't know what goes in here."}
        ),
    version="0.0.1"
    )
bucket_create = create_bucket.ApiBucketCreate(
    "test_bucket",
    compress=True,
    encrypt=False,
    policy=bucket_policy
    )
bucket = create_bucket.sync(client=api, json_body=bucket_create)

if not isinstance(bucket, ApiBucket):
    raise 