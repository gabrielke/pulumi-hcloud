// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package hcloud

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Define services for Hetzner Cloud Load Balancers.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-hcloud/sdk/go/hcloud"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := hcloud.NewLoadBalancer(ctx, "loadBalancer", &hcloud.LoadBalancerArgs{
// 			LoadBalancerType: pulumi.String("lb11"),
// 			Location:         pulumi.String("nbg1"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = hcloud.NewLoadBalancerService(ctx, "loadBalancerService", &hcloud.LoadBalancerServiceArgs{
// 			LoadBalancerId: pulumi.Any(hcloud_load_balancer.Test_load_balancer.Id),
// 			Protocol:       pulumi.String("http"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type LoadBalancerService struct {
	pulumi.CustomResourceState

	DestinationPort pulumi.IntOutput                     `pulumi:"destinationPort"`
	HealthCheck     LoadBalancerServiceHealthCheckOutput `pulumi:"healthCheck"`
	Http            LoadBalancerServiceHttpPtrOutput     `pulumi:"http"`
	ListenPort      pulumi.IntOutput                     `pulumi:"listenPort"`
	LoadBalancerId  pulumi.StringOutput                  `pulumi:"loadBalancerId"`
	Protocol        pulumi.StringOutput                  `pulumi:"protocol"`
	Proxyprotocol   pulumi.BoolOutput                    `pulumi:"proxyprotocol"`
}

// NewLoadBalancerService registers a new resource with the given unique name, arguments, and options.
func NewLoadBalancerService(ctx *pulumi.Context,
	name string, args *LoadBalancerServiceArgs, opts ...pulumi.ResourceOption) (*LoadBalancerService, error) {
	if args == nil || args.LoadBalancerId == nil {
		return nil, errors.New("missing required argument 'LoadBalancerId'")
	}
	if args == nil || args.Protocol == nil {
		return nil, errors.New("missing required argument 'Protocol'")
	}
	if args == nil {
		args = &LoadBalancerServiceArgs{}
	}
	var resource LoadBalancerService
	err := ctx.RegisterResource("hcloud:index/loadBalancerService:LoadBalancerService", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetLoadBalancerService gets an existing LoadBalancerService resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetLoadBalancerService(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *LoadBalancerServiceState, opts ...pulumi.ResourceOption) (*LoadBalancerService, error) {
	var resource LoadBalancerService
	err := ctx.ReadResource("hcloud:index/loadBalancerService:LoadBalancerService", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering LoadBalancerService resources.
type loadBalancerServiceState struct {
	DestinationPort *int                            `pulumi:"destinationPort"`
	HealthCheck     *LoadBalancerServiceHealthCheck `pulumi:"healthCheck"`
	Http            *LoadBalancerServiceHttp        `pulumi:"http"`
	ListenPort      *int                            `pulumi:"listenPort"`
	LoadBalancerId  *string                         `pulumi:"loadBalancerId"`
	Protocol        *string                         `pulumi:"protocol"`
	Proxyprotocol   *bool                           `pulumi:"proxyprotocol"`
}

type LoadBalancerServiceState struct {
	DestinationPort pulumi.IntPtrInput
	HealthCheck     LoadBalancerServiceHealthCheckPtrInput
	Http            LoadBalancerServiceHttpPtrInput
	ListenPort      pulumi.IntPtrInput
	LoadBalancerId  pulumi.StringPtrInput
	Protocol        pulumi.StringPtrInput
	Proxyprotocol   pulumi.BoolPtrInput
}

func (LoadBalancerServiceState) ElementType() reflect.Type {
	return reflect.TypeOf((*loadBalancerServiceState)(nil)).Elem()
}

type loadBalancerServiceArgs struct {
	DestinationPort *int                            `pulumi:"destinationPort"`
	HealthCheck     *LoadBalancerServiceHealthCheck `pulumi:"healthCheck"`
	Http            *LoadBalancerServiceHttp        `pulumi:"http"`
	ListenPort      *int                            `pulumi:"listenPort"`
	LoadBalancerId  string                          `pulumi:"loadBalancerId"`
	Protocol        string                          `pulumi:"protocol"`
	Proxyprotocol   *bool                           `pulumi:"proxyprotocol"`
}

// The set of arguments for constructing a LoadBalancerService resource.
type LoadBalancerServiceArgs struct {
	DestinationPort pulumi.IntPtrInput
	HealthCheck     LoadBalancerServiceHealthCheckPtrInput
	Http            LoadBalancerServiceHttpPtrInput
	ListenPort      pulumi.IntPtrInput
	LoadBalancerId  pulumi.StringInput
	Protocol        pulumi.StringInput
	Proxyprotocol   pulumi.BoolPtrInput
}

func (LoadBalancerServiceArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*loadBalancerServiceArgs)(nil)).Elem()
}
