// parse api data to table and plot elements
// Market plot interface for exploration of the data
// used function

var ParserAPI = React.createClass({
    getInitialState: function () {
        // initialized to N/A for display
        return {
            offers: [],
            periods: [],
            phases: [],
            players: [],
            treatment: [],
            auction: [],
            player_stats: [],
            group: [],
        };
    },
    fetchData: function () {
        $.ajax({
            type: "GET",
            url: "/anl/analysis_data",
            success: function (data) {
                // TODO: check data completness

                // destring and jsify dates
                for (var key in data.periods) {
                    if (data.periods.hasOwnProperty(key)) {
                        var date_string = data.periods[key].updated.replace("Z", "")
                        var split_space = date_string.split("T")
                         var split_date = split_space[0].split("-")
                         var split_time = split_space[1].split(":")
                           data.periods[key].updated = new Date(split_date[0], split_date[1]-1, split_date[2], split_time[0], split_time[1], split_time[2].split(".")[0]);
                    }}
                 for (var key in data.phase) {
                    if (data.phase.hasOwnProperty(key)) {
                        var date_string3 = data.phase[key].created.replace("Z", "")
                        var split_space3 = date_string3.split("T")
                         var split_date3 = split_space3[0].split("-")
                         var split_time3 = split_space3[1].split(":")
                           data.phase[key].created = new Date(split_date3[0], split_date3[1]-1, split_date3[2], split_time3[0], split_time3[1], split_time3[2].split(".")[0]);
                         // console.log(data.phase[key].id, split_date3[0], split_date3[1]-1, split_date3[2], split_time3[0], split_time3[1], split_time3[2].split(".")[0], split_time3[2].split(".")[1],  data.phase[key].created  )
                    }}
                  for (var key in data.offers) {
                    if (data.offers.hasOwnProperty(key)) {
                        var date_string = data.offers[key].created.replace("Z", "")
                        var split_space = date_string.split("T")
                         var split_date = split_space[0].split("-")
                         var split_time = split_space[1].split(":")
                           data.offers[key].created = new Date(split_date[0], split_date[1]-1, split_date[2], split_time[0], split_time[1], split_time[2].split(".")[0]);
                        // cleared date only for cleared offers
                        if (data.offers[key].cleared == true) {
                            var date_string2 = data.offers[key].timeCleared.replace("Z", "")
                            var split_space2 = date_string2.split("T")
                            var split_date2 = split_space2[0].split("-")
                            var split_time2 = split_space2[1].split(":")
                            data.offers[key].timeCleared = new Date(split_date2[0], split_date2[1] - 1, split_date2[2], split_time2[0], split_time2[1], split_time2[2].split(".")[0]);
                        }
                    }}

                this.setState({
                    offers: data.offers,
                    periods: data.periods,
                    phases: data.phase,
                    players: data.player,
                    auction: data.auction,
                    treatment: data.treatment,
                    player_stats: data.player_stats,
                    group: data.group,
                });
            }.bind(this)
        });
    },

    componentWillMount: function () {
        this.fetchData();
    },

    render () {
        return (
            <div>
                Showing auction {this.state.auction.id}, created {this.state.auction.created}
                <div>
           <Table_main
                    offers = {this.state.offers}
                    periods = {this.state.periods}
                    phases = {this.state.phases}
                    players = {this.state.player}
                    auction = {this.state.auction}
                    treatment = {this.state.treatment}
                    player_stats = {this.state.player_stats}
                    group = {this.state.group}
           />

    </div>
                  <div id="market">
                      <Market
                       offers = {this.state.offers}
                    periods = {this.state.periods}
                    phases = {this.state.phases}
                    players = {this.state.player}
                    auction = {this.state.auction}
                    treatment = {this.state.treatment}
                    player_stats = {this.state.player_stats}
                    group = {this.state.group}
                      />
            </div>
                       <div>
           <Table_main2
                    offers = {this.state.offers}
                    periods = {this.state.periods}
                   phases = {this.state.phases}
                    players = {this.state.player}
                    auction = {this.state.auction}
                    treatment = {this.state.treatment}
                    player_stats = {this.state.player_stats}
                   group = {this.state.group}
           />

    </div>
            </div>

                    )
                }
});

// render to div id="cost_tables"
ReactDOM.render(<ParserAPI/>, document.getElementById("main"));

