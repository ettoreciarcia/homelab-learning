package main

import (
	"fmt"
	"net/http"
	"os"

	"github.com/gin-gonic/gin"
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

func main() {
	router := gin.Default()
	router.GET("/albums", getAlbums)
	router.GET("/helloWorld", helloWorld)
	router.GET("/env", getEnv)
	router.GET("/envs", getEnvs)
	router.GET("healthCheck", healthCheck)

	router.Run("localhost:8080")

}
