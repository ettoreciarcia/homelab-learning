package main

import (
	"context"
	"fmt"
	"log"
	"net/http"
	"os"

	"github.com/gin-gonic/gin"
	"github.com/minio/minio-go/v7"
	"github.com/minio/minio-go/v7/pkg/credentials"
)

// album represents data about a record album.
type album struct {
	ID     string  `json:"id"`
	Title  string  `json:"title"`
	Artist string  `json:"artist"`
	Price  float64 `json:"price"`
}

// albums slice to seed record album data.
var albums = []album{
	{ID: "1", Title: "Blue Train", Artist: "John Coltrane", Price: 56.99},
	{ID: "2", Title: "Jeru", Artist: "Gerry Mulligan", Price: 17.99},
	{ID: "3", Title: "Sarah Vaughan and Clifford Brown", Artist: "Sarah Vaughan", Price: 39.99},
}

type path struct {
	Path        string `json:"path"`
	Description string `json:"description"`
}

var paths = []path{
	{Path: "/helloWorld", Description: "A sample Hello World response"},
	{Path: "/getAlbums", Description: "Get all albums in a json"},
	{Path: "/getEnv", Description: "Get a specified env"},
	{Path: "/getEnvs", Description: "Get all env"},
	{Path: "/healtCheck", Description: "Health Check"},
	{Path: "/helloPerson", Description: "Testing query string"},
	{Path: "/", Description: "List all available path"},
}

// getAlbums responds with the list of all albums as JSON.
func getAlbums(c *gin.Context) {
	c.IndentedJSON(http.StatusOK, albums)
}

func helloWorld(c *gin.Context) {
	var Test = "Hello World"
	c.IndentedJSON(http.StatusOK, Test)
}

func getEnv(c *gin.Context) {
	env := os.Getenv("TESTENV")
	c.IndentedJSON(http.StatusOK, env)
}

func getEnvs(c *gin.Context) {
	for _, pair := range os.Environ() {
		fmt.Println(pair)
		c.IndentedJSON(http.StatusOK, pair)
	}
}

func healthCheck(c *gin.Context) {
	c.String(http.StatusOK, "Health Check returns status 200")
}

func helloPerson(c *gin.Context) {
	firstname := c.DefaultQuery("firstname", "Guest")
	c.String(http.StatusOK, "Hello %s", firstname)
}

func home(c *gin.Context) {
	c.IndentedJSON(http.StatusOK, paths)
}

func listBucket() {
	endpoint := os.Getenv("MINIO_ENDPOINT")
	accessKeyID := os.Getenv("MINIO_ACCESS_KEY")
	secretAccessKey := os.Getenv("MINIO_SECRET_KEY")
	useSSL := false

	// Initialize minio client object.
	minioClient, err := minio.New(endpoint, &minio.Options{
		Creds:  credentials.NewStaticV4(accessKeyID, secretAccessKey, ""),
		Secure: useSSL,
	})
	if err != nil {
		log.Fatalln(err)
	}

	log.Printf("%#v\n", minioClient) // minioClient is now setup

	buckets, err := minioClient.ListBuckets(context.Background())
	if err != nil {
		fmt.Println(err)
		return
	}
	for _, bucket := range buckets {
		fmt.Println(bucket)
	}
}

// func testMinio(c *gin.Context) {
// 	c.(http.StatusOK, listBucket)
// }

func main() {
	router := gin.Default()
	router.GET("/albums", getAlbums)
	router.GET("/helloWorld", helloWorld)
	router.GET("/env", getEnv)
	router.GET("/envs", getEnvs)
	router.GET("healthCheck", healthCheck)
	router.GET("/", home)
	router.POST("/helloPerson", helloPerson)
	// router.GET("/testMinio", testMinio)
	router.Run("0.0.0.0:8080")

}
