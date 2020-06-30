// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 *  Provides a Hetzner Cloud Load Balancer Network to represent a private network on a Load Balancer in the Hetzner Cloud.
 */
export class LoadBalancerNetwork extends pulumi.CustomResource {
    /**
     * Get an existing LoadBalancerNetwork resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: LoadBalancerNetworkState, opts?: pulumi.CustomResourceOptions): LoadBalancerNetwork {
        return new LoadBalancerNetwork(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'hcloud:index/loadBalancerNetwork:LoadBalancerNetwork';

    /**
     * Returns true if the given object is an instance of LoadBalancerNetwork.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is LoadBalancerNetwork {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === LoadBalancerNetwork.__pulumiType;
    }

    public readonly enablePublicInterface!: pulumi.Output<boolean | undefined>;
    public readonly ip!: pulumi.Output<string>;
    public readonly loadBalancerId!: pulumi.Output<number>;
    public readonly networkId!: pulumi.Output<number>;

    /**
     * Create a LoadBalancerNetwork resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: LoadBalancerNetworkArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: LoadBalancerNetworkArgs | LoadBalancerNetworkState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as LoadBalancerNetworkState | undefined;
            inputs["enablePublicInterface"] = state ? state.enablePublicInterface : undefined;
            inputs["ip"] = state ? state.ip : undefined;
            inputs["loadBalancerId"] = state ? state.loadBalancerId : undefined;
            inputs["networkId"] = state ? state.networkId : undefined;
        } else {
            const args = argsOrState as LoadBalancerNetworkArgs | undefined;
            if (!args || args.loadBalancerId === undefined) {
                throw new Error("Missing required property 'loadBalancerId'");
            }
            if (!args || args.networkId === undefined) {
                throw new Error("Missing required property 'networkId'");
            }
            inputs["enablePublicInterface"] = args ? args.enablePublicInterface : undefined;
            inputs["ip"] = args ? args.ip : undefined;
            inputs["loadBalancerId"] = args ? args.loadBalancerId : undefined;
            inputs["networkId"] = args ? args.networkId : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(LoadBalancerNetwork.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering LoadBalancerNetwork resources.
 */
export interface LoadBalancerNetworkState {
    readonly enablePublicInterface?: pulumi.Input<boolean>;
    readonly ip?: pulumi.Input<string>;
    readonly loadBalancerId?: pulumi.Input<number>;
    readonly networkId?: pulumi.Input<number>;
}

/**
 * The set of arguments for constructing a LoadBalancerNetwork resource.
 */
export interface LoadBalancerNetworkArgs {
    readonly enablePublicInterface?: pulumi.Input<boolean>;
    readonly ip?: pulumi.Input<string>;
    readonly loadBalancerId: pulumi.Input<number>;
    readonly networkId: pulumi.Input<number>;
}