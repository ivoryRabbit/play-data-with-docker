curl -XPUT "http://localhost:9200/test_idx/_doc/1" -H "Content-Type: application/json" -d '{"name": "DGLee", "message": "Hello, world"}'

curl -XGET "http://localhost:9200/test_idx/_doc/1"

curl -XDELETE "http://localhost:9200/test_idx/_doc/1"

curl -XPOST "http://localhost:9200/test_idx/_doc/1" -H "Content-Type:application/json" -d '{"name": "DGLee", "message": "Hello, world"}'

curl -XPOST "http://localhost:9200/test_idx/_update/1" -d '{"doc": {"message": "Hi, kibana"}}' -H "Content-Type:application/json"

#curl -XPOST "http://localhost:9200/test_idx/_bulk/1" -H "Content-Type:application/json" -d '{"index":{"_index":"test", "_id":"1"}}{"field":"value one"}{"index":{"_index":"test", "_id":"2"}}{"field":"value two"}{"delete":{"_index":"test", "_id":"2"}}{"create":{"_index":"test", "_id":"3"}}{"field":"value three"}{"update":{"_index":"test", "_id":"1"}}{"doc":{"field":"value two"}}'