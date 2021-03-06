// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package hcloud

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides a Hetzner Cloud Load Balancer Network to represent a private network on a Load Balancer in the Hetzner Cloud.
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
// 		lb1, err := hcloud.NewLoadBalancer(ctx, "lb1", &hcloud.LoadBalancerArgs{
// 			LoadBalancerType: pulumi.String("lb11"),
// 			NetworkZone:      pulumi.String("eu-central"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		mynet, err := hcloud.NewNetwork(ctx, "mynet", &hcloud.NetworkArgs{
// 			IpRange: pulumi.String("10.0.0.0/8"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = hcloud.NewNetworkSubnet(ctx, "foonet", &hcloud.NetworkSubnetArgs{
// 			IpRange:     pulumi.String("10.0.1.0/24"),
// 			NetworkId:   mynet.ID(),
// 			NetworkZone: pulumi.String("eu-central"),
// 			Type:        pulumi.String("cloud"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = hcloud.NewLoadBalancerNetwork(ctx, "srvnetwork", &hcloud.LoadBalancerNetworkArgs{
// 			Ip:             pulumi.String("10.0.1.5"),
// 			LoadBalancerId: lb1.ID(),
// 			NetworkId:      mynet.ID(),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type LoadBalancerNetwork struct {
	pulumi.CustomResourceState

	EnablePublicInterface pulumi.BoolPtrOutput `pulumi:"enablePublicInterface"`
	Ip                    pulumi.StringOutput  `pulumi:"ip"`
	LoadBalancerId        pulumi.IntOutput     `pulumi:"loadBalancerId"`
	NetworkId             pulumi.IntOutput     `pulumi:"networkId"`
}

// NewLoadBalancerNetwork registers a new resource with the given unique name, arguments, and options.
func NewLoadBalancerNetwork(ctx *pulumi.Context,
	name string, args *LoadBalancerNetworkArgs, opts ...pulumi.ResourceOption) (*LoadBalancerNetwork, error) {
	if args == nil || args.LoadBalancerId == nil {
		return nil, errors.New("missing required argument 'LoadBalancerId'")
	}
	if args == nil || args.NetworkId == nil {
		return nil, errors.New("missing required argument 'NetworkId'")
	}
	if args == nil {
		args = &LoadBalancerNetworkArgs{}
	}
	var resource LoadBalancerNetwork
	err := ctx.RegisterResource("hcloud:index/loadBalancerNetwork:LoadBalancerNetwork", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetLoadBalancerNetwork gets an existing LoadBalancerNetwork resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetLoadBalancerNetwork(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *LoadBalancerNetworkState, opts ...pulumi.ResourceOption) (*LoadBalancerNetwork, error) {
	var resource LoadBalancerNetwork
	err := ctx.ReadResource("hcloud:index/loadBalancerNetwork:LoadBalancerNetwork", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering LoadBalancerNetwork resources.
type loadBalancerNetworkState struct {
	EnablePublicInterface *bool   `pulumi:"enablePublicInterface"`
	Ip                    *string `pulumi:"ip"`
	LoadBalancerId        *int    `pulumi:"loadBalancerId"`
	NetworkId             *int    `pulumi:"networkId"`
}

type LoadBalancerNetworkState struct {
	EnablePublicInterface pulumi.BoolPtrInput
	Ip                    pulumi.StringPtrInput
	LoadBalancerId        pulumi.IntPtrInput
	NetworkId             pulumi.IntPtrInput
}

func (LoadBalancerNetworkState) ElementType() reflect.Type {
	return reflect.TypeOf((*loadBalancerNetworkState)(nil)).Elem()
}

type loadBalancerNetworkArgs struct {
	EnablePublicInterface *bool   `pulumi:"enablePublicInterface"`
	Ip                    *string `pulumi:"ip"`
	LoadBalancerId        int     `pulumi:"loadBalancerId"`
	NetworkId             int     `pulumi:"networkId"`
}

// The set of arguments for constructing a LoadBalancerNetwork resource.
type LoadBalancerNetworkArgs struct {
	EnablePublicInterface pulumi.BoolPtrInput
	Ip                    pulumi.StringPtrInput
	LoadBalancerId        pulumi.IntInput
	NetworkId             pulumi.IntInput
}

func (LoadBalancerNetworkArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*loadBalancerNetworkArgs)(nil)).Elem()
}
