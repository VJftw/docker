# S3 Sync

## Environment variables

* `SOURCE`: e.g. `s3://bucket`
* `DESTINATION`: Can leave blank, and mount local/shared volume into `/data`
* `SCHEDULE`: e.g. `* * * * *` will sync DESTINATION to SOURCE every minute.

This container will first synchronise the source to the destinate upon launch, then backup the destination to the source.
