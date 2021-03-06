// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

export function getNetwork(args?: GetNetworkArgs, opts?: pulumi.InvokeOptions): Promise<GetNetworkResult> {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("hcloud:index/getNetwork:getNetwork", {
        "id": args.id,
        "ipRange": args.ipRange,
        "labels": args.labels,
        "name": args.name,
        "withSelector": args.withSelector,
    }, opts);
}

/**
 * A collection of arguments for invoking getNetwork.
 */
export interface GetNetworkArgs {
    readonly id?: number;
    readonly ipRange?: string;
    readonly labels?: {[key: string]: any};
    readonly name?: string;
    readonly withSelector?: string;
}

/**
 * A collection of values returned by getNetwork.
 */
export interface GetNetworkResult {
    readonly id?: number;
    readonly ipRange?: string;
    readonly labels?: {[key: string]: any};
    readonly name?: string;
    readonly withSelector?: string;
}
