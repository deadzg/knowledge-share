# Deprecating the older APIs:
- Announce the end-date on your website's blog
- email developers
- In your API docs, include a message/banner on all pages which mentions the end-date
- X-API-Warn For notifiying the consumers
- X-API-Deprecation-Date: 2019-12-25T00:00:00Z
- X-API-Deprecation-Info: https://abc.com/old-api-deprecated-info?utm=from-header
- When the final day arrives for the API Producer, it's best to slowly or intermittently shut down the endpoints. 
- If possible, use a "rolling blackout" approach, where your endpoints return an HTTP 410 "Gone" for a short period of time (like a few minutes) every two hours
- Use a gradual process of migrating users from the old integration to the newer one, to identify whether any "edge cases" are present
- see if it's possible to roll it out in parallel, and monitor for differences between the old and new
- Let the client know to watch for X-API-Deprecation-* headers in the logs
- For APIs, once a version is no longer usable, any calls made to it will be defaulted to the next oldest, usable version.
- We refer to an API call made without specifying a version as an unversioned call. An unversioned call will always point to the oldest available version. 
- You can specify older versions in your API calls as long as they are available and your app has made calls to that version. For example, if your app was created after v2.0 was released and makes calls using v2.0, it will be able to make calls to v2.0 until the version expires even after newer versions have been released. If you created your app after v2.0 but did not make any calls until v2.2, your app will not be able to make calls using v2.0 or to v2.1


## Resources:
- https://zapier.com/engineering/api-geriatrics/
- https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/410
- https://developers.facebook.com/docs/graph-api/changelog/4-30-2019-endpoint-deprecations
- https://developers.facebook.com/docs/apps/versions
- https://cloud.google.com/blog/products/api-management/restful-api-design-tips-versioning