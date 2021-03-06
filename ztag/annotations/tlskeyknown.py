from ztag.annotation import *

class TLSKnownKey(Annotation):

    protocol = protocols.HTTPS
    subprotocol = protocols.HTTPS.TLS
    port = None

    tests = {
        "known_key":{
            "tags":["known-private-key", ]
        }
    }

    # Certificate fingerprints for certificates with know private keys
    # https://github.com/sec-consult/houseofkeys/

    FINGERPRINTS = set(['007fdaa8c08e250b5587ae9a49345a5c41e971cf3a52242670fc8bfb2e6d75ab',
                        '0179bddd57628de9aed3ee7963f07fabd1a9bb0a793f7af51adacedee625b015',
                        '02980519c55e5dfb06656a7ea8ef7342553b6c95e4f9c5ea242b0f14398e4f90',
                        '0343cd1d23f19a26eaf82e73dd89408c64432e5ede3b9927221ab1465a0ef701',
                        '03804c07a542330344396e92e4668bbb0bbefefa78ba6c74a80d9e3b3f219703',
                        '03d61a6cfd45f4123ad18df7f4297997d030554658ab53b5c8e305895de071a4',
                        '042faf6b5578ba4f33892e00e96836581acbd6e9dc03f9962f479fd1d6bd5445',
                        '06f29b4e6eac32323dfc372eff55150a901ea2ee1c287c50ef99856c786c072b',
                        '0ae4db801bb55c0f939e04e74edb177509b735534e7b734f246c48c704aad502',
                        '0b566c676bacfd62d1ae74bc3b8502a4405cd316d172b845ad3b4305c354dc8c',
                        '0cd8c08b9672c0e232a8edc510acdeedaee816a494622dc5a64b8e0bcba580fe',
                        '0e0505d9667e3da1a73ccf4264d1dae38223bc6ac159f66e2fb600c6a8f65299',
                        '0f1b486c96d6f1db6e5004a19482071ece5b8669069c8dd7f2239d8f732b6b72',
                        '10359839b1e49ba55951b3c41c2457f32c739c387bcf290af89e9600ca7755b7',
                        '11ef973af2dcdafc15469849307fbbd66b350a71e0bfb36c5c84e24be7cc77bf',
                        '121c838be8c0406a3ccd8dcaa7febf36331f43b7a709f207315b8c6844ef8375',
                        '12fe03e2d05700dce2a21300b89032c4bf329220d9e4dae8131bb31101bdbc09',
                        '132d2ce4d3a55c73aa5bf95c671e9c0e87f0ab9d3c34782dc8f9162fc713fc31',
                        '13657bfa2c9cdba7591f97675f203a8bad4ecbe3f70fbaccad43646dec3b600d',
                        '136c268a6680631acd46dcb643edd876f66525e8ba0e72561489812a490ed55d',
                        '1578652bc72b52439c4f24dcc7c13a7137e57111da899e5b63365792971b9c9d',
                        '167390050a67bb785bb01b0934bcc57b4865593ae98b2f09a002e496a69cebde',
                        '16853a59c2c6349cb6234a7fccfbb9135468acccff8436ef8295af2ae9daaa50',
                        '17e1063806d29ecafe5cb793bc637173f395e3446623d7a4a02ca92aebd1f944',
                        '180b1952e696258fbfd5825142578ddb781e416974ae1405587d73c881fdf204',
                        '1819d09d4b9a024153abb4e4bb2db6aa45ef23f3b02281b9e1cecc659de1693e',
                        '182034cb65b46a7a8563262995120630392b1f5d626133d961503056c1c72c1a',
                        '1a1eba50e3f0534fdf76efbad3d9a2227233438e815baaf88640ce428675f053',
                        '1a2c64abf243770a2164e694e567d07e8a2e91aeed2826a945247eeaf78f5c49',
                        '1aae24bc2d5e0efc03d0500f3e0a0d569a28b78544d2503ecf3807d42dde0b25',
                        '1ac24caf29271e7e2847979a5a0f8908d7bce0a852c4407d5271b8a63afa081f',
                        '1b581b1079831c47c5b24760149505a8328d36a8f954bf8c2722eb50193f7ccd',
                        '1bdc7e7f57abff690fe31c66cfcb1f8a52deba9f3da032e290a6634b712c9d2d',
                        '1c3a57a64d13174ab5a59acb78a27127351bbed0fba5fde283f89bc76db6aa54',
                        '1c912745cf1b97543af1d73f35e9709461b951b86ef4a9143d7a0343b5be2da9',
                        '1cc3ba2e8aa103d1c41e752e12773b17e7c716298eed0dcf15d32c17080248ec',
                        '1d12450a59d208ccc9fa490af9498acd7ac7b5bd7c329c261eb3c635330637d5',
                        '1d4aadf8925fd597951c60119ed33e88f4994548ffa72c92790b0fe7b2c2d0b6',
                        '1f2f8b736aa3886fee322ad5ab96e8adcfb7cdfbcb61e4bfbab140fbdaedf666',
                        '1f354a14019011983ccdc786e95ab75c9e5ec79213e5ba7b07ebaeed922a78a3',
                        '1f65b547819c038b70f73c7b58f41bb57f93d84a259386e38402b82ce762c4ba',
                        '22c87c507b3086205f50b78dc59832a81d4f8a73a802c6aca1c94ff083d7d0ff',
                        '22fc8f4ec8525a55b249d4b3daaf087c7e7c9300cba9ec7c7e221c0993a8f69c',
                        '23756c87c3e65a4d09d07f5b0093b72a8ab5852b16bea95e80f293ca38e2ad61',
                        '24907cc88b454819daf9f552f17b1c23f5bffacb5d51406dcbe19a30bbe3c62f',
                        '263446e06f41e569590dd5eb224a7fe4e7b249ecd737f74a754b61f08842b974',
                        '264a63820c8e6b231c7f5983239e93b34c577f02513d4d06fae9782044e087f7',
                        '2660c49d12ffee7e63bad87aa64ea8dd5a0468c2f07f6c9681a959f96ba68502',
                        '268bcce65b4cfe7e15e3c9d2d60e1f325bf7e09ecad254f3acc44ec40ac9955f',
                        '26b336d85b19d9aa07067eb11e66926f433bcebfda41cd85474f396164618a69',
                        '276172c4901e1f69f7a4634e7ea7f2b034c87ffcbf02c884f0f24d55f9a77b64',
                        '27fdf2a38cd3b9dfe6c85e59178e661f059821e6ad8c506f50986088b2c129ad',
                        '28fec0593a81984721720da0fe3bda4f31000df87ea3223ec77cdabfaa8ff05f',
                        '2b784f9d8a8a67f1c2d50315fb2e67329961fad409a6647b84c8c48600f76712',
                        '2e61c214104f54bce5685cd10e46194cd3881a05f0214a3c88beb2945e33a50d',
                        '2e92a483ca9fa188691f78bed85b12fe73f816b41ea0b25e5bb148a0a2924d18',
                        '2eb7ce965e13f5e549c5ba236a94d71f807a847719a0c9b8737422059e59d63b',
                        '2ece680cbd0d58afdcc53156a629cdcdba02c4755195322e45cd101bbc14691c',
                        '2eff496179bc11ed1802526483e6eda3b8ca4a96af4054532811feb5f4e78d56',
                        '30ada332d9c6f9e10dda3e9b2a129e105637d8533eaa05f2484af14d212918cb',
                        '32436581269c7394d8f824aca956bbbfaf513afb914f1c196bc32db0810994b0',
                        '328a743d5c80fb6f00e77424f71118512c580f043197f33c4c37eee483506b77',
                        '3345b9e437ee7f045aca9e78eb1c7a157d1ef2a7efa55508d071366616ed0d41',
                        '351747b9cbcf79aac5cb398a4734a8db87e4b6487998c32129366c326c08ce61',
                        '37d402b57b918992c5982462040a675a5fda023a5c60e63baca003bd11709aff',
                        '3976441c8dbdfa569b342f8aff1b5af2b9ac2a4c6e49713b2b3dc0d8295ce893',
                        '39f7ecde2160e664bf494f445a9fe5a70bcee5d04671dd62d33251bed4bb516c',
                        '3a275acd6477e509d94f74a911828c7925269bf904424ee992a623b176f139d6',
                        '3a681b04fcaf08e4151a09036ebb6e1375e8b0eb28bc31cfd3ee552f85aa0d31',
                        '3b08c01868b44a26427cc65074ddae2720cf975e39a2c5faa071dd0b25e842d1',
                        '3b47a34404f2e3b7ff21607759f516ad30fe84a28cca92e4bfba1433f4ec8f13',
                        '3c6eabcf19da166c0137086cf101846a8a8dde3c28bad4d8fa5c80bc56570612',
                        '3dbd6706ed5c8372a6b773417fe733f545c8589e16d2942de4465720e50900d0',
                        '3df297030ea4ab86a1e58d3455c729df700a574b37f4b8b0e1d5dc769e40fdb9',
                        '3e0f16396bb13e4f0885c65f100dcb2c25c2914ed04ac22906bd55e3a7b3b706',
                        '414ce31fa403e89a3fa8ba4f3d246b81b534821cc875a652a77cbedf0a0dbf62',
                        '414e61fc1f7e17b4d5f4becfedd80bfb8a1c7944182ccdf51e2d419ce874dd19',
                        '415ff4742721fd2888a33cd45c36d07dcc4794878ba229431439313674ed2dd1',
                        '423f3282b1650c64471d06e23a47c795e2e7c844c5b86eb79f7dccab0174ef01',
                        '42b85dd61894ea2a99bb8172603b3736776a8094a86d39de23deacdd273c0275',
                        '4403880b9cba3f740154a274418dc3435a5c1b57ca728b3387da568bacc803f1',
                        '45587266ab88d1b558762be87a5f082826fdfdbd2f0c87d88fc7ca1de953953d',
                        '464f4fcd90934c66b83509dffaa8993922520a7a14422853060a6a2c289d3ecb',
                        '465f11059ed20927060d03637a9f0c00759e2033007475541e2d302cb1042883',
                        '469fdecc085bed13d54f61391a3456742f33aff7422cde13fb3506bb149dac38',
                        '47d208c30f7d66ef4a716aad4c40ed6b26a2d3d2c12276354365bd1d463ca82c',
                        '47fa89956f2aa349e8814b21a7bbd64c9b597f0f192bfe073559945a7a846534',
                        '482a90cad250f9d40c5ca923252f780a9d432722cf9a5d955ef893a3fd7455e5',
                        '48981842223ceb1ffc744153f82c977dc2cb1120e54af89c9ec4ecb96308b715',
                        '4a847195e581e1609a55308819c45ad96c84a8b08fbd91ad03388ea9ba30479e',
                        '4bb02dcd8c477920c2619ebc1737045420631d5aa970b372e984c56187c0a6c7',
                        '4c69bf0a31e6f1e617470b8b4b75e1cda8d935ebd7448a18e6fbace5f1349b8c',
                        '4d2adcad7e1bc9eafcad8810b557f5000db73c60c16112121aa217a462ecd2b9',
                        '4d56421bea15a441b6377e81c9c6a13ef094f663fedcace162e8e5d73d0c0f2d',
                        '4d6e34a157e0aff0230053da7b798c0f26a212d8030d0d3903e1ace17505b7a7',
                        '4e0db6ad2f6a3195562bc621c52da241158259048c593cb00e2534731973ef2d',
                        '50b17d0ab33df4533bc469b21fa6b6dbfee53f741e7a01650164bb05c555f800',
                        '5146b9adfe8736e631e44bb8a1af27a7c1d45854a29fb3e6cd67814c125f1ba7',
                        '515c56709528aa1ff49ab2822958d317ddfc34f6fccb973fa8a207f8916b8379',
                        '51a9e6d7f769f3864a530c4311c5c2ec5d40b499dc89c2cbe3ce2c5423844f7a',
                        '51ab293c9fe391eeeb1a2739de15cd8029e3033142962c6c386f2da78d03a945',
                        '5228b5f98a23d3b34194ca76e0623dc84c906819a79611994159477191099af8',
                        '52aafa625913949299094855f598c0990b1f41c042058a9a0fc9be8c4d7aab85',
                        '52f614ec03ed306cf34ae7315f181a59172ece8eb8c656bc6ea9537a082e73bf',
                        '533424b1d73fa18c68a3849b792b7bbb596019d1fc2dc3e56a6fdad76fdb8798',
                        '53696bcf35c57934d624c2a0ae6233cadf86c367ef7b58ac660a92bd7c7e1dac',
                        '53a3219d03145026235e60f2bc701d0a02cbc11b3ae9b459f183d77b21d38713',
                        '564b58f351adb624884b301a3f92d845cf2cf9de531ce7c35a9aadc181380904',
                        '5684f906c71a3fc3c389ca348806b36af0d873e0e77aa8a7738a0f0630fafacf',
                        '56c4f4cba93b12e9274e5e8b472a2a5535fbe5dbd92c94c051ffc06ed3dcbdbb',
                        '56e486049b2e98943759d2fe25fe24a4f2460c2e39e8761f8e3db9b250d3ed6a',
                        '5722d7cd625f59e0459a7f77825ec1b0222695d00a13c3767a4486b5014c44eb',
                        '574339119218fba1ab3d6bbb96bc931b9be7f694a4c91551bd65656142b48555',
                        '574db3497efb9efddcbca4edbcb3c28dc3d72ae30f6f7657f0bbf490561cdcf8',
                        '5755a149dfc3f00e6d213bfdae18968148ca9b0991a2c192169b840be9d5a696',
                        '5824fddeb960835418ec3f8d6c069b90053d3289dfafb63708c3f188713d13f1',
                        '59433163cb501ba312d184de81efd38ae20a68a28c3920792f668565195f8b3f',
                        '5b23e3d38d1a78b85f1d054818e5d0a91c06e3376bfffd389f60c22295b5240a',
                        '5e9381fd1334dfa8188c37c2b62d5ce8927ae7abb1c0bb57c1bb78c82279d038',
                        '5fa98ba264f7d4794b2c6fb2165cf27fc71284c06e7b057efb7b1b9c8859429c',
                        '60a81c43e5a583d2b450ed96b7bd1309ff5441daca07ffedab3c619dc907bf06',
                        '60d00b3cfb5bb8a6d936bab40ef5c3c1970d3cd06dfddd09936e9527f6f2e68d',
                        '60da89d322a875d12cadee237478a53d83b60cd388c27f1311650534286e3e88',
                        '614b9c3b062ffe8d6b936de84494ace7a3f7753257fb1a66dafba79753d80c0d',
                        '61d76d42946ac1e4f2c38172b103199b830c8b49ddedbe7ab7ba6ea38248b8e6',
                        '61ee367df84c0953d0e67ab9e144a2f68d3ebfa92f9d49bec50a220b3ed7ecb3',
                        '620fb2c557b17a4d6846821a0c2760c82548d66f5998391e1e133b49f617a43e',
                        '633d92a66b461db92c623f15a4bf687405dc527f5662706d7300aea6a7e52973',
                        '6612628da3f7134d4e21c7aff7cc0acefd709d35a12435480853cd79aab4c8b9',
                        '66502cf4627ca24d54be86cc7e239da5407b70cf12adc0224f2c704519f4291f',
                        '6655b3ddb55e3f37a6742ca25028444d2fd74a01b2545dcda879a68309448fd3',
                        '67cb6953df4dbc8a9bf28e49c790ced0f052d58053737247b6cb1f2a7bcebfee',
                        '68046de77f7a251f86789ea333d3ed1ff7f9b44f1d621971ac6a281e8e9d402b',
                        '68cc2ef42231142fef04dd701a9e9a4a39416f5c54d309e5e5203423256b97f4',
                        '6ad4ab39d3406b3c8fa6d6aef3450229232ddfb1752e4dbbdf76dbfdd82ced1a',
                        '6b4cf15ea316bb24fd37768eabf30cd9f069489f12db8710bcb5f399eace034b',
                        '6b80fcfa4f422f645225170a644845fd6343003b55ecdb2643c837f969a13d34',
                        '6be565144fdbf69a4f8b4b3d70fa4b81d5946ad6fe40a25c13f4751aa6ed4044',
                        '6d4bb616fc43e34822dd0d3591bc8d5d4a7f9b2d3122cef105d10cc36f5ea925',
                        '6d6130e70257848ddb88436f54ec8f443d3d434927ce9c35cc92af7debf64837',
                        '6e8cad9bbca0c452ab851f9470bc56c4f0722df0e1b7ecc4c06b684fc8bf6793',
                        '715b2da7784e4c09d6bf9aae621d067c42fc2a6008f00f44ee99af81dc86a3bb',
                        '719195c289c0e5361ab5952932085883eb0503bcc01738096684204ddaf48ccf',
                        '726dafa7bbc22df34b7061c220d0280717aa6849718a2e7c3e5f78468bc8cafd',
                        '738523c7102fdd44124bb4a36075adfcb35dceb1f947ea56ea2366192d9e6482',
                        '73a335ea26dd43ed29032ed97287d41f993a62d639b8aaf111e77edbcd299ac0',
                        '741de224f41b702f10a5543bd7625ea730c2545bf2ffdb53bfe17deb9e65518c',
                        '74a0c278e504711836282fd497100c8b2d4afdc631c5de9348f0b010899d35da',
                        '7596222ef48c0da3e1bc0014119a5fb22d88fd2858ada3d1091efefd346e8832',
                        '75b93088101a2a9521e39980ea41f0bcc3fbd3b43c4b33cb50e9bbc1d5ffdfd0',
                        '75bfa53adaaf8a2d7654cb8d7152525de8d58d8509de404ebf9bdb3b25f53ea3',
                        '76dedd416489a69368a5311bfc14ee3a24282e0a417b13852f61d9718dba4861',
                        '771212f3186622c16a380ef193f268b23259fab540646e37c93ebbedefffa11d',
                        '78fd13c7325a78b9600b589eef1cbca79d91fb93a50aa1e6339535aeb7c1c300',
                        '7a0cdfba4c3d30f005ab7545a7c9f2b70734be7f5246852254e53be9aee5cb48',
                        '7ada8534e11cb1f29930b5346f970803163013eff15bc838c9137d3d232f0f12',
                        '7bbcd8908a19345a69e1f0d420ace432e934121fdd45b0f8b72357eaddd18748',
                        '7c0567eb411254309dbf5e271a6442db9d3ceea526644732e637a17ae42a7c3f',
                        '7c36df2230d9ab675ebf59deb09a6b1c73af932d39b597873981cc202df01d8e',
                        '7d56d33439c1c937983d7b9045702cf255392df8a698ad1fe06143dfa2c0a4f3',
                        '7de3fec5d6aed41a9ec51db95fe8410af066136c4f763d3210859d79c69bcaac',
                        '7e24a9cf0fb89f8597ce21655c7b39a04d913f21653f85b886187cfa6c5c1c70',
                        '7fc0931794cd1ec2f414835c657992288d5e6f87aefacbc63e84daa4089830cd',
                        '7fedb5cdf4d0fac463d90521b79910c7fa72e0d6306652646202886e050d3950',
                        '7fee2d2c5f6ecc1f3ef58cbcbfb4e92b9b0c6f9d5aca0b0f2730f99ed3b6965c',
                        '813ef18b596950a7a8724c5eb27674cb9e2a049265cdbd37174023a7fc9b9a1d',
                        '816735d1fd53b8747aa3a61e277dd8fd5dd303475bc9730ead8ad67155518e33',
                        '8180fc02fd62e8e9415c0173566bd3ad21d9970bc81c806755b731279de9194f',
                        '821f3f7c769af3c37710144c5a9baff0f8581a3f22628e01bdad6fa9c3798687',
                        '829a7b73e18486f87d8426f574987793078e326c7837300f1684902b72512bda',
                        '83640aa264389f7170fa3083e19d6d84d10810679e8356eec123a350ee80b5be',
                        '8418c73cd0583f5b3fa7f1ccf24960e747ea6c8b340afc96359afca7dcdcacec',
                        '85f9a5108ec3eb34dbb2fb2b7dbe10bdd8c46e2ca97bb1a26a23eb2f36b06e23',
                        '86071fee0d0196e561717661356b36e89780e871bff69ae0fe9dd79de482d68d',
                        '860c614afc30fb91510f597281f05c8d1d18789ca084614b1daf7a7d7c9778d3',
                        '88adfda86ac1d9a04f013dae4dcb7941e522636fc7fa50eaf1ae0954cea9a085',
                        '89b855b24e004244d61077eae44584e3012ed572dc1b299505b8eb2489683fa0',
                        '8b34030ee356195cafe3c12783a132280e1bded5d557f00c7c2b87703dbdf4f8',
                        '8cd058ff7e2204f05498ccdaa86560c61cb111bfc69e1682e82d0bdc21192cd8',
                        '8dfcdda83dfccb8e8441eae99f6fefc86740ce11ca259a16dff2929e87e3d801',
                        '8e14ac1b76bde6ba19d4ef1b3516b169e629b31bb94cec07bfc8c8b31438e3ee',
                        '8f65c15394371a53943783a9df43d4e2f47e28a7ce933465936e0b75f37fddb5',
                        '8ffa88876555864c22c79f12273aa4e97ade65a92876cf61991e66a0252d5d06',
                        '90d371553024736b91091d0b4db2670fcd7124d903c80588b5e11bf4f89ca948',
                        '90db9821efdaae7af64871f9096b1b2ad3f4ff65620b6f2574629a02f4f03ea8',
                        '939791981f2c5c4d99e13fc661b6d9a3404450cb50bcf1cfe5c1d38c4069dc38',
                        '93ebc44f1e20c02d4b2556f2fd6a0fec0d4687f8d58fabe6e2abc4ebe91ca62a',
                        '94d4b664af7846fe3f715691f475fbcbb11c5a2b3762ee43b25edbdb86fc3c7f',
                        '95f15db592ce2bcce22dda23683e65e9a438ef37e1b558264de195bb9b9d782a',
                        '96197cd06e4fc5ea57764cb79e85f34a5655f2e3426f70d06bebaa9f1093f407',
                        '96da7af22342b706872b5b2469d90790fa10efc5158bdd587765437b6ab021f0',
                        '991c0cd22a6df18fe6aff30ec0f59f90c23739c58adfe0ac747f13d0fdaa4228',
                        '99c815f27893387fbb53580718c4ee9ea87cf45fbcf2ee4c1769687594074e9a',
                        '9a65b2ff681b841615d010beee41a78d72dd7917a33c9c58a355b3ebbe33192b',
                        '9b86f11e961a7e435626c95375c0385ddabd700038d3e564c04963a97660db4f',
                        '9d55f83f458d7dd70cb4d4526e81f92795ba58fcf11739154c2a0bbb7cebb2d0',
                        '9f3a099e620290ca15b51e6c2500223117cc956a3ebc7eee53315b14261c913e',
                        '9f4607359d315bd176c9268ea8dec61069bd24c83545a4bd1e4adb732b35a24f',
                        '9f691cf4208556b6398faaae29c23fbddb12ecb072d2d44e3322ce3448f7866e',
                        'a03b2079d382c9024a7b4c9fbbbd60e243fedd793f78b7b8027a82c4b2f599da',
                        'a04f3465bc3c57c4b7871b1dccd3a8b2215062fc1bb0b8f4ab173fdf4263f261',
                        'a117f4c9a6391bdf2d7442eb0512a058e83f8bf814726f88776ba0377825a69a',
                        'a32e796ebe20716626e3b301c8edd55106d981f98cd9eedbd68a715472ac0d06',
                        'a4a6b5a448b04836953f2e42ed1d860353acf703c0f7ddbf194c5f834e896214',
                        'a503e393473e54b524d46312c02467cae6bc59e786284e6ddea79d6596840f12',
                        'a5d9e7c00df5315fa4b8951888a2c98f3f3187f403a3bf50620384fd2d05dd10',
                        'a6503f1151705e027b1c069689b99e314a0321ae65c9434e59d99ccfa087b9c7',
                        'a693b5952ba3c74033569a74f8b5460b0354d81db096c41669e16fa898a31ff2',
                        'a769cfb6324bada915f96c96f60bd0c98a6b0bc579e57fd06ef3cffec74c780e',
                        'a831e11a00b786bb3c277676e67821d4009f74603f9ac7bd1d10feccb63e601d',
                        'a89075cd85ea68face4135b0df7f9a972e562b6ddbc3f05c713b5f400907527b',
                        'a8dc3a4b18b74fe962de4a4c5ff51c667b92f07ac1b7d04fd311c1c88939790c',
                        'a9746ac7c8f864fbd3827dbebe5b48fbb1c102a5bfc329f920524c4b6736bc53',
                        'a9832741eca1aaaedbfc0ba2abd0493b755fe08a4dd7d3338916e40d0d3d1975',
                        'a9e7b74d648e8ccaff46591483dfc645a72ef593e8fa00666464073757bedbf2',
                        'a9f036644c0b947b8f592e0769acba04ea2e277a512c6bd1f429997d16cfecb6',
                        'aa31d64400d3ef30e421dbbbc8fbe50b4319fe4fa28b27cb078ee240c4eeec93',
                        'aab25b16156139aca76b32b7aa2a7837e8439897b892741963963a8fe9f2bf96',
                        'ac848ff728ccb8f9e600ee76ffcb032bc53dc5b3cd9e9fa0cdc9b65a2760446c',
                        'ad49b195f050e72ea993472a06c38fdd9228812dfe6668d161b7fe64df8b0883',
                        'adcf87a27bf65ec6ef0d7863267741a736f2034a8a58cbdb5c5917077fe3795f',
                        'add3ed0480efd2749e71a236e7b77751e476693b054ec98d3d4c6d567cde99d7',
                        'ae827ab48e93fb56e096b07e2effe98b1a3b7ab9a778ef8ed5898f55cc9ff91c',
                        'b116b6cc5d022fa5d609fb4b38239adae3487ed9f94b835fcd036643cb1590a9',
                        'b145d44dcca311f33edcc5f27aad7cd5e590952cd2c95ab3471887a3f3b0d04c',
                        'b18fb98402028476926763d0e7da29bd545e3b84e5a36561792b77ad8f4e276b',
                        'b1993a3bf1456cea057a0753d5dc8cf6bfcb11d7a8ebaf8d4d1a39097b3bcc9e',
                        'b1cc105448e4e015cfd1a0caf1c1436773c7996ad8e6c8b3993a8afcaf25d4c0',
                        'b249e7b79671bc5f29044f70d8036e06026981b8b1b3c5a4656fcca78752a885',
                        'b26c8de004003b2cfcfdf78131dfdad2c77896e1d6ae09b244a951a8b29185a2',
                        'b287a5e8d15b8b943fae1bc471661874c9dc8ff5cf1589ce1debc353223fd8d6',
                        'b3cb97f5e6bf0ee2a09331bbdec71b770a3fb092bf05b347d6c2e1dbc56a1579',
                        'b43a2d6de1612df00e74e279906a5951757a5ebf849153e18517cc4acfac0b46',
                        'b55024cbfd78156ddfc1dedb71cc97ff28ae2454109e51778763bb6881d25773',
                        'b5addb3caf8bf4105d86e3e0230ea9d06d61e1fe610f3741b6a997fa5a2acf95',
                        'b73c50a2d3be3b9fba5e2e9e4c9cb86f98deb6b0a808d67fe8b0d2584dfb9600',
                        'b80bbb8d0fdd4d1a32515270abc19f0566ac13bc2f8603739237bfb266a88901',
                        'bc719c1e0ee3efc6745f080b1431d4c8c41517dc4ef6343540f84efeb20f6f21',
                        'bcafedfb57711f360cc998ac3733e752762c8bfb3b232adebf4c745c0b9eb982',
                        'bd05b4701829759d464bd357b44fe4e466db76b8212ef78d91ca53876173f8ab',
                        'bdc20333264aaf9030172ec3a611177edd15c13acea52cf4b28526e5e51244b5',
                        'bdf633be4288c40fc56e5aab1787e2c357dcf2cb9f62843ccea363f82dfb1cd9',
                        'be501670dfc0fdbd46ddfecdfdc07c81e2374a28b4f29523d461a4c52475ac10',
                        'be9d4e9046da50bf41474e51768da49cbd51f7c00297bcd39b45acae3ba900ed',
                        'bfdd9295642b25555e1ee251a4c1b9da8f10bf33c41d0bf0cafe40b5e120745d',
                        'bff017db05cd8ddbb4098667a9566044b9b40552cd699a6974138090f6189579',
                        'c01fc8b2a651a9966636dd2f80ecced9d7c0557f029f9bb9b8271fea42408b12',
                        'c04a416c6c2317baebe286842fdcfb07a9b2ec929e77a076da3fc6c697757689',
                        'c2562c3b5dd60c3e73037e4f4d1ddadd86587d545e82fbde511a30998bcdff55',
                        'c3ebe12824c6f099d5649d5d11b3cfa0b725ef622f3fbb90d3c6cb986f57251b',
                        'c3ef3fa7a44267f7adf9f2dab1f405bf87290a7cf253255b79f6070ddf14ba3b',
                        'c5e82a59dc7b421be1569f2d35eacebde26651da588a5da18f8d5a73b6652071',
                        'c6b84db64fd1d61514f8c8885e37b53f1fe0bea6c517573b0cb58aa4fedc3e56',
                        'c71cf7fe775717450cdc04289de0372d4446e547f21d90330fe1eb840f017d34',
                        'c8ba4204c27931d47ad464c4e87957670509ae8f831dbfcf2c8566cc4267210c',
                        'c8dc463ac414a199ad84d9c0e752049e8b2935bbc431b0a704d968403358f884',
                        'ca29d98eb8a83c1b2dee8e11befc8d83573b7fe636187e2ab1a70baba59eca99',
                        'ca7fee3f9a6fc0c9b67444940c7f344d5389803c040b1e21664dab18f776bd7d',
                        'cacec835b3b340b121982e92edc920927ac82c3821351b085ed8f2bc89a76ed9',
                        'cb36482dc97fe9dfafb4cc75d8f6bf2571a7c6d8bcc0716e6072c79576261f8a',
                        'cb56256893f253eed317e7d55fe023627e92390c4cb9a988276bc771f3b09cba',
                        'cb7b2370f35a5b93fc5bcebaff540b73b5cdd987ee8749979557a334dfaefb8b',
                        'cbe7614e06865be50376ba161574246f7c70390c26e94096db6fe296d3f62bb9',
                        'cc54b0cbba94daee6cb2631dc44dcc6a6d6690be4afc57bc4569ff738e6a3b24',
                        'cc6c74117c3849b49e4f9ccc451649b49ced4ad5075f4ff7f4fadb1d41ef34a1',
                        'cdf0bafebd86ff87df3ee8e69528fcec658acbd82fbb8cd450ebeef1d62f0216',
                        'ce74f649d4e7324ca236adf0b229116037595bbcd252c448c3e1a56379f95e44',
                        'cea5f4b8b3096e7ecb10b009a1d4ad0b0a2c7a8314cba9244c513cb2ca9e24eb',
                        'cfbcd663804637b4f66294863e27e37c97340189d6a34c8008c89e1b0441a2a8',
                        'd1c94c5c475d55201e46da54d0835a4c3a88324643e8d429a12d6a59eede6c3d',
                        'd1e0b01a2d6057e7d483d66697618e1050702b23445e1de0fb9305bc43fdf8dd',
                        'd20f8029eb272f67baab6c852e2ad009b8be99309291e0df43e0dff9d6578705',
                        'd2445e8249ac1d5a5e21d7412dfa3f421da40865c4b3a47c9ded2d9c5fee527d',
                        'd26038b6ea855102f192980ac65d1165dc110448344fe8fc414d08c23cb45f31',
                        'd28b07042ddd783f80485cf25ef5d08fec259cb3df2377f9c17d6e41bba2fdb5',
                        'd5c0101d5ac007024e50477188b03d76f28112472edf56c5e19a76cf069008e7',
                        'd736a2545de3821542a2d2d19415c3aaff2f62db9c84e5106f17ba4b15dbffc2',
                        'd794d4614abeba490958403711ea3560f898cfb50c32cfc73fa1ba027f38645b',
                        'd7acc1eee3c33e40d805b8249ea505387dec1716120702922a63722d5f44019a',
                        'd8bf49a6597e3a962f73190ba897f19706ef569bb8ee9c0fcc18147afc6eca55',
                        'daed718b6cd5d2c73716d5288998b87ebdb5a5208c34ed873556245bf3b95532',
                        'dbe28ce74a73d838169cce62ba8cd052fe9ab8badf1ccb6c7f8a224e1b7e0654',
                        'dc24d2c5cb9271083ec400dbac2210a7285fd5b09ba70b71ea5aaeeea4830ffe',
                        'dd7bb83d48709dc9064c742460cef928735cc6f446c2db0f5f1c4aba6cfba2dc',
                        'dd9c9d473cdcaec293e38462891209ce4c714efe7a0c2714975740043c1b4e83',
                        'dde06fa4e9d03d18653eb5416856a0afa00ebdeec4fe8311d3e58ae86e12584c',
                        'dea7a4f4ed3493b1439ed20bd35e52fe493c2002e5ce00d94c09c538b401e0fd',
                        'dedff5f97a5b8a619d80791802efc85d75de042cc3d9eddb882826588c26d0ee',
                        'df3d7be3f31f68dd3f49bf62d85fd3d517a5851682184f0d77f2f13e05906bd1',
                        'df45c2bf89da44a13a5e7eb1c1b1c40cb2526a85c36eef7ba847e3b323a0a8d2',
                        'df9eea87e05c36648fd76b421d452704c87d5e0c046dd6efc458308e84017f55',
                        'e0178277c8d6720a54cc5e84e534e93722ef2cfa3337a34bf0319680155268b8',
                        'e020ac519a4ee6d7025c54a5b4f6bb5e19be29bb22bcc382e77da60d8b1d46f8',
                        'e09db495bf00cafc5cf96e763fbae96237290ee003c9d4b3bfecce10f8bb4c35',
                        'e254902ef38abfba260935095ac862fab3d530d49c2cbe98c78f7a74877026b7',
                        'e3e8069f9174ec82ffcaf320395df910ea1c2c58a9a9f943e8f22ee5384d7142',
                        'e4d09f84810efa9ad8541b7a820f094408ef760744ffe44d397f88d28b441995',
                        'e5190badcca6d5dbf7425180267926a8324fd79cad647b2ef4f8d9d3230f2216',
                        'e6d86a8f1a5e910e77223b3f78b1e2c89736259750b5c58c7d5a10981c39d139',
                        'e7948464af040bd95abafad04d4994d425e4a0e132bf6bc8e3a24ef986c6fc56',
                        'e88cf5e48005af8d4b80521374aa668267771dce5ccde6b5576d66455c10b7f7',
                        'e98c65e8f67bbe8b4d72b076e5483e2e3d36598db1c77cfae3588c72cfe7aeec',
                        'ea1b916b9e7c5aa7d217b1f4d0ad0fc979977b57157c07de3afb28f7bb21c162',
                        'ea7c29a2e3dee9c6dea693cd218069998a79c2da5735f499070d6fb3256fc79e',
                        'ebd895021b1fdbe132745ef7cef78ebf1e80b6ba4c1d59734278e9ed445b9a78',
                        'ebf0103bd97b5decd4b694efa0fdabbc68dd60c6735a8486bb38b6886ed81261',
                        'ebf7d1f907abfe9cedbbd6bf8f67b4be060d99530e0487361da4a4cb407e2ef9',
                        'ecae05b4ac08b5de3940c0b757bb1f2dba87f041d7b652484e51044b2be776e6',
                        'ed3e2dca4abd09a4aa9d0dd2a5a0559c15cf91f72a0a09dc08232a61b6ae67bd',
                        'ee9c29789dfecb221bc1f5e490df587b1d4e56e065a04401283b0ebf2e8dd697',
                        'ef91f71d4d2774351fe66a61deabf53d1abfd8d6ffda000a944b0d2e44ea412c',
                        'f019c609001336dae1928aeafc8bccc46d65adb519a12d82077c04d309953dc4',
                        'f0602545e96ae10246571d480446283f0f16bc384f34af2858cb183bb32dc0e0',
                        'f3f0b000d320fcfa1fd315b5d8e929f667e4654bd61c43c589877b7741746b49',
                        'f4238706a4c1a3459274471b566ae0597c8cea5337eeff4693017b7eb2162406',
                        'f4a73f510573f8398de96c4a6f047637c5e34e1883c55124e4ae5af5de2d934f',
                        'f5b73c22771813c34480bc2d1bf9695198fa530eb18a3982985ed96ead304515',
                        'f6b2ae13b57d00c33b600ea9f8408b12872f91f0a7674a146136f7d8ba0fb7af',
                        'f6e432b5ad06200b051cfbc072b6c95b5421508d974c8b4b6e58cfac024513f5',
                        'f8b59af047dc914188550179b17177ced23853d74d29cef4611652863dc48793',
                        'f973624da2997470faaceeb7bffb20562a3b4abd3698ee87a0743e6f252c0779',
                        'fa4e09c8056cd10d36e6c03e5bb37e3f55e27dd346300aa95de0c7d706abe1b0',
                        'faebc680aece7e2fac8ab8f1970efc9b90cba64f91ad52dd19bd6e39cacc091c',
                        'fb64e0c2cb746211f9a4baec70c5610f51c47d52fa38007a1b9cc475bb2f4c6c',
                        'fbec92b68f6d6359c55506f70dd27368a01524b7e936527ec345da3cff9554f8',
                        'fcd10d720e85a956bc97aa4ed7f6b2915e8affb3ee1f1d32a2a2c9382c3c0df8',
                        'fcdae3841d10b6d18ebf758980a712b5de38819b308e2b2e20f49430f134d54b',
                        'fd0dfb45e83cb17028bf40e357dd186c1588505bc7607cadaf2dca273b72d104',
                        'fd53927cb1d86b7e7f73f9ceb379b81226b8504f90889e7b52d4c00fdb4410f0',
                        'fe78cd65a75349ca37fa94492f14e9144814b3bfa54ac18a7d222d03223bd17b',
                        'ffa9998f9bf034b2cfe3810991b57793c4b9aa0e3c5aa01de204fa2a243893ae'])

    def process(self, obj, meta):
        s = obj["certificate"]["parsed"]
        if s["fingerprint_sha256"] in self.FINGERPRINTS:
            meta.tags.add("known-private-key")
            return meta
        return None
