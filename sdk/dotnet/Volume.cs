// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.HCloud
{
    /// <summary>
    /// Provides a Hetzner Cloud volume resource to manage volumes.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using HCloud = Pulumi.HCloud;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var node1 = new HCloud.Server("node1", new HCloud.ServerArgs
    ///         {
    ///             Image = "debian-9",
    ///             ServerType = "cx11",
    ///         });
    ///         var master = new HCloud.Volume("master", new HCloud.VolumeArgs
    ///         {
    ///             Automount = true,
    ///             ServerId = node1.Id,
    ///             Size = 50,
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// </summary>
    public partial class Volume : Pulumi.CustomResource
    {
        [Output("automount")]
        public Output<bool?> Automount { get; private set; } = null!;

        [Output("format")]
        public Output<string?> Format { get; private set; } = null!;

        [Output("labels")]
        public Output<ImmutableDictionary<string, object>?> Labels { get; private set; } = null!;

        [Output("linuxDevice")]
        public Output<string> LinuxDevice { get; private set; } = null!;

        [Output("location")]
        public Output<string> Location { get; private set; } = null!;

        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("serverId")]
        public Output<int> ServerId { get; private set; } = null!;

        [Output("size")]
        public Output<int> Size { get; private set; } = null!;


        /// <summary>
        /// Create a Volume resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Volume(string name, VolumeArgs args, CustomResourceOptions? options = null)
            : base("hcloud:index/volume:Volume", name, args ?? new VolumeArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Volume(string name, Input<string> id, VolumeState? state = null, CustomResourceOptions? options = null)
            : base("hcloud:index/volume:Volume", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Volume resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Volume Get(string name, Input<string> id, VolumeState? state = null, CustomResourceOptions? options = null)
        {
            return new Volume(name, id, state, options);
        }
    }

    public sealed class VolumeArgs : Pulumi.ResourceArgs
    {
        [Input("automount")]
        public Input<bool>? Automount { get; set; }

        [Input("format")]
        public Input<string>? Format { get; set; }

        [Input("labels")]
        private InputMap<object>? _labels;
        public InputMap<object> Labels
        {
            get => _labels ?? (_labels = new InputMap<object>());
            set => _labels = value;
        }

        [Input("location")]
        public Input<string>? Location { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("serverId")]
        public Input<int>? ServerId { get; set; }

        [Input("size", required: true)]
        public Input<int> Size { get; set; } = null!;

        public VolumeArgs()
        {
        }
    }

    public sealed class VolumeState : Pulumi.ResourceArgs
    {
        [Input("automount")]
        public Input<bool>? Automount { get; set; }

        [Input("format")]
        public Input<string>? Format { get; set; }

        [Input("labels")]
        private InputMap<object>? _labels;
        public InputMap<object> Labels
        {
            get => _labels ?? (_labels = new InputMap<object>());
            set => _labels = value;
        }

        [Input("linuxDevice")]
        public Input<string>? LinuxDevice { get; set; }

        [Input("location")]
        public Input<string>? Location { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("serverId")]
        public Input<int>? ServerId { get; set; }

        [Input("size")]
        public Input<int>? Size { get; set; }

        public VolumeState()
        {
        }
    }
}
