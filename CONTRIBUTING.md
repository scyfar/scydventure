# Contributing to Scydventure

A big welcome and thank you for considering contributing to Scydventure! We love your input!

We want to make contributing to this project as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the mod-pack
- Submitting a fix
- Proposing new features

Reading and following these guidelines will help us make the process easy and effective for everyone
involved.

## General contribution information

Contributions are made to this repo via [issues][issues], [discussions][discussions] and
[pull requests (PRs)][pulls].
A few general guidelines:

- To report security vulnerabilities, please write a mail to
  [our team](mailto:scyfar@pm.me?subject=%5BINCIDENT%5D%20scydventure%20-%20)
  and do not report it via issues or discussions.
- Search for existing issues, discussions and PRs before creating your own.
- Provide a detailed description and all necessary information required for your concern.
- For non-trivial changes, create a [discussion][discussions] first.
- PRs must address a single concern in the least number of changed lines as possible.
- Changes to the code are introduced using the [GitHub flow][github-flow].

### Discussions

[Discussions][discussions] are an informal way to talk about changes or to ask questions about the
project.

They are great to start a conversation about a planned change and to get other opinions/solutions
for a problem.

### Issues

[Issues][issues] are the formal way to report bugs or request new features.

To work efficiently with [issues][issues], all the necessary information must be added in the
description, especially error logs and version information.
Adding a description of how to reproduce a bug or what the expectations for a new feature are does
help, too.

It is considered a good practice to first open an issue and give the team time to respond, before
contributing changes for it.

### Pull Requests (PRs)

Changes are introduced using pull requests with aforementioned [GitHub flow][github-flow]. \
Here is a quick overview over the workflow:

1. Fork the project
2. Clone your fork
3. Create a branch for your changes
4. Make your changes
5. Push your changes to your fork
6. Create a pull request

An ongoing effort when contributing is to ensure your fork is up-to-date and that your changes are
made on top of the latest changes in the upstream project.

## Release

> [!NOTE]
> Currently, this pack focuses on distributing via [Modrinth](https://modrinth.com/) and for the
> [NeoForge](https://neoforged.net/) mod loader only.
> Other platforms and loaders _may_ follow. No promises though.

Releases are automated with GitHub actions based on Git tags.

The process uses scripts provided in the [`scripts` directory](scripts/). These are optimized to
work on Linux. See the respective script for a description of what it does and how to use it.

The requirements for the script are available in the `requirements.txt` and can be installed with

```shell
pip install -r scripts/requirements.txt
```

To create the mod-pack file
([`mrpack`](https://support.modrinth.com/en/articles/8802351-modrinth-modpack-format-mrpack)),
the tool [`packwiz`][packwiz] is used.

### Release process

The following steps must be performed to create a release.

1. Ensure the `./packwiz/[...]/[...]/.modlist.json` is up-to-date with the new versions entries

   - **This file also must have entries for all dependencies**
   - It is used for the attribution data
   - It is used to add mods to the mod-pack

2. Run the [script to add mods](scripts/add-mods.py)

   - **This script deletes everything from the `mods` folder**
   - Do not install dependencies with `packwiz`
     - Unfortunately, this is a manual task

3. Run the [attribution script](scripts/attribution-data.py) and add the data to the
   [`ATTRIBUTION.md`](ATTRIBUTION.md)

4. Make manual changes to the mod-pack files, if necessary

   - e.g. set the `preserve` flag in `index.toml`

5. Write/update the `./packwiz/[...]/[...]/CHANGELOG.md`

   - This changelog is player facing, not technical
   - The markers are important as these are used in the GitHub action to extract the information
   - There may already be a changelog present with a `NEXT` version for the pack. This must be used
     and the version changed to the actual release version. This changelog may not be complete.

6. Run the [release script](scripts/release.py)

   - The `<git_tag>` argument will be the new version and must follow the format
     `<pack-version>_<minecraft-version>_<loader-name>`
   - The `<new_draft_version>` is the version that will be set for the next iteration and is usually
     a `-draft` version

> [!NOTE]
> The release type is determined from the Git tag name.
>
> - `draft` will cause the release to be marked as a draft and nothing will be uploaded to Modrinth.
> - `alpha`, `beta` and `rc` will cause the release to be marked as pre-release and uploaded with
>   the respective type to Modrinth. `beta` and `rc` will both be considered a beta release.
> - If no suffix exists, it is considered a regular release and will be also uploaded to Modrinth as
>   such.

<!-- link references -->

[discussions]: https://github.com/scyfar/scydventure/discussions
[github-flow]: https://docs.github.com/en/get-started/using-github/github-flow
[issues]: https://github.com/scyfar/scydventure/issues
[packwiz]: https://packwiz.infra.link/
[pulls]: https://github.com/scyfar/scydventure/pulls
