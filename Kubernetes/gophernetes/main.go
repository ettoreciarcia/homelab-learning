package main

import (
	"context"
	"fmt"
	"reflect"

	corev1 "k8s.io/api/core/v1"
	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
	"k8s.io/client-go/kubernetes"
	"k8s.io/client-go/tools/clientcmd"
)

func main() {
	// Load the kubeconfig file
	config, err := clientcmd.BuildConfigFromFlags("", "/Users/ettoreciarcia/.kube/kind")
	if err != nil {
		panic(err)
	}

	// Create a Kubernetes client
	client, err := kubernetes.NewForConfig(config)
	if err != nil {
		panic(err)
	}

	// Create a ConfigMap object
	configMap := &corev1.ConfigMap{
		ObjectMeta: metav1.ObjectMeta{
			Name: "my-config-map",
		},
		Data: map[string]string{
			"key1": "value1",
			"key2": "value2",
		},
	}

	// Create the ConfigMap in the default namespace
	result, err := client.CoreV1().ConfigMaps("default").Create(context.TODO(), configMap, metav1.CreateOptions{})
	if err != nil {
		panic(err)
	}

	fmt.Printf("ConfigMap created: %s\n", result.GetObjectMeta().GetName())
	fmt.Printf("ConfigMap data: %s\n", result.Data)
}

// create a funnction to check 2 configmap contenet are the same
func checkConfigMapContent(configMap1, configMap2 *corev1.ConfigMap) bool {
	return reflect.DeepEqual(configMap1.Data, configMap2.Data)
}
