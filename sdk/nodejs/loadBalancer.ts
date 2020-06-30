// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 *   Provides a Hetzner Cloud Load Balancer to represent a Load Balancer in the Hetzner Cloud.
 */
export class LoadBalancer extends pulumi.CustomResource {
    /**
     * Get an existing LoadBalancer resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: LoadBalancerState, opts?: pulumi.CustomResourceOptions): LoadBalancer {
        return new LoadBalancer(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'hcloud:index/loadBalancer:LoadBalancer';

    /**
     * Returns true if the given object is an instance of LoadBalancer.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is LoadBalancer {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === LoadBalancer.__pulumiType;
    }

    public readonly algorithm!: pulumi.Output<outputs.LoadBalancerAlgorithm>;
    public /*out*/ readonly ipv4!: pulumi.Output<string>;
    public /*out*/ readonly ipv6!: pulumi.Output<string>;
    public readonly labels!: pulumi.Output<{[key: string]: any}>;
    public readonly loadBalancerType!: pulumi.Output<string>;
    public readonly location!: pulumi.Output<string>;
    public readonly name!: pulumi.Output<string>;
    public /*out*/ readonly networkId!: pulumi.Output<number>;
    public /*out*/ readonly networkIp!: pulumi.Output<string>;
    public readonly networkZone!: pulumi.Output<string>;
    public readonly targets!: pulumi.Output<outputs.LoadBalancerTarget[]>;

    /**
     * Create a LoadBalancer resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: LoadBalancerArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: LoadBalancerArgs | LoadBalancerState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as LoadBalancerState | undefined;
            inputs["algorithm"] = state ? state.algorithm : undefined;
            inputs["ipv4"] = state ? state.ipv4 : undefined;
            inputs["ipv6"] = state ? state.ipv6 : undefined;
            inputs["labels"] = state ? state.labels : undefined;
            inputs["loadBalancerType"] = state ? state.loadBalancerType : undefined;
            inputs["location"] = state ? state.location : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["networkId"] = state ? state.networkId : undefined;
            inputs["networkIp"] = state ? state.networkIp : undefined;
            inputs["networkZone"] = state ? state.networkZone : undefined;
            inputs["targets"] = state ? state.targets : undefined;
        } else {
            const args = argsOrState as LoadBalancerArgs | undefined;
            if (!args || args.loadBalancerType === undefined) {
                throw new Error("Missing required property 'loadBalancerType'");
            }
            inputs["algorithm"] = args ? args.algorithm : undefined;
            inputs["labels"] = args ? args.labels : undefined;
            inputs["loadBalancerType"] = args ? args.loadBalancerType : undefined;
            inputs["location"] = args ? args.location : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["networkZone"] = args ? args.networkZone : undefined;
            inputs["targets"] = args ? args.targets : undefined;
            inputs["ipv4"] = undefined /*out*/;
            inputs["ipv6"] = undefined /*out*/;
            inputs["networkId"] = undefined /*out*/;
            inputs["networkIp"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(LoadBalancer.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering LoadBalancer resources.
 */
export interface LoadBalancerState {
    readonly algorithm?: pulumi.Input<inputs.LoadBalancerAlgorithm>;
    readonly ipv4?: pulumi.Input<string>;
    readonly ipv6?: pulumi.Input<string>;
    readonly labels?: pulumi.Input<{[key: string]: any}>;
    readonly loadBalancerType?: pulumi.Input<string>;
    readonly location?: pulumi.Input<string>;
    readonly name?: pulumi.Input<string>;
    readonly networkId?: pulumi.Input<number>;
    readonly networkIp?: pulumi.Input<string>;
    readonly networkZone?: pulumi.Input<string>;
    readonly targets?: pulumi.Input<pulumi.Input<inputs.LoadBalancerTarget>[]>;
}

/**
 * The set of arguments for constructing a LoadBalancer resource.
 */
export interface LoadBalancerArgs {
    readonly algorithm?: pulumi.Input<inputs.LoadBalancerAlgorithm>;
    readonly labels?: pulumi.Input<{[key: string]: any}>;
    readonly loadBalancerType: pulumi.Input<string>;
    readonly location?: pulumi.Input<string>;
    readonly name?: pulumi.Input<string>;
    readonly networkZone?: pulumi.Input<string>;
    readonly targets?: pulumi.Input<pulumi.Input<inputs.LoadBalancerTarget>[]>;
}