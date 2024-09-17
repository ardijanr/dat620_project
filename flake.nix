{
  description = "Development environment";
  inputs.nixpkgs.url = "github:nixos/nixpkgs";
  inputs.flake-utils.url = "github:numtide/flake-utils";

  outputs = { self, flake-utils, nixpkgs }:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
      in
      {
        devShell = pkgs.mkShell {
          buildInputs = with pkgs; [
            pkgs.python311Packages.flask
            pkgs.python311Packages.torchvision
            pkgs.python311Packages.torchaudio
            pkgs.python311Packages.torch
            python311Packages.sentencepiece
            python311Packages.accelerate
            python311Packages.transformers

            (
              pkgs.python311Packages.buildPythonPackage rec {
                  pname = "mlc-ai-nightly";
                  version = "0.15.1";
                  format = "wheel";
                  src = fetchurl {
                    sha256 = "sha256-/CNKbs2SBoJscEiAxECCMqjUH1mqt4cvjvwwGhcjLT8=";
                    url = "https://github.com/mlc-ai/package/releases/download/v0.9.dev0/mlc_ai-0.15.1-cp310-cp310-macosx_10_15_x86_64.whl";
                  };
                  buildInputs = [  ];
                }
              )
          ];
        };
      }
    );
}
