var notepad = {
    notes: [],
    selectedId: null
};

var nextNodeId = 1;

var onAddNote = function () {
    var note = {id: nextNodeId, content: ''};
    nextNodeId++;
    notepad.notes.push(note);
    notepad.selectedId = note.id;
    onChange();
};

var onChangeNote = function (id, value) {
    var note = _.find(notepad.notes, function (note) {
        return note.id === id;
    });
    if (note) {
        note.content = value;
    }
    onChange();
};

var onSelectNote = function (id) {
    notepad.selectedId = id;
    onChange();
};

var NoteSummary = React.createClass({
    render: function () {
        var note = this.props.note;
        var title = note.content;
        if (title.indexOf('\n') > 0) {
            title = note.content.substring(0, note.content.indexOf('\n'));
        }
        if (!title) {
            title = 'Untitled';
        }
    
        return (
            <div className="note-summary">{title}</div>
        );
    }
});

var NotesList = React.createClass({
    render: function () {
        var notepad = this.props.notepad;
        var notes = notepad.notes;
    
        return (
            <div className="note-list">
                {
                    notes.map(function (note) {
                        return (
                            <div key={note.id} className={notepad.selectedId === note.id ? 'note-selected' : ''}>
                                <a href="#" onClick={this.props.onSelectNote.bind(null, note.id)}>
                                    <NoteSummary note={note}/>
                                </a>
                            </div>
                        );
                    }.bind(this))
                }
            </div>
        );
    }
});

var NoteEditor = React.createClass({
    onChange: function (event) {
        this.props.onChange(this.props.note.id, event.target.value);
    },

    render: function () {
        return (
            <textarea rows={5} cols={40} value={this.props.note.content} onChange={this.onChange}/>
        );
    }
});

var Notepad = React.createClass({
    render: function () {
        var notepad = this.props.notepad;
    
        var editor = null;
        
        var selectedNote = _.find(notepad.notes, function (note) {
            return note.id === notepad.selectedId;
        });
        
        if (selectedNote) {
            editor = <NoteEditor note={selectedNote} onChange={this.props.onChangeNote}/>
        }
    
        return (
            <div id="notepad">
                <NotesList notepad={notepad} onSelectNote={this.props.onSelectNote}/>
                <div><button onClick={this.props.onAddNote}>Add note</button></div>
                {editor}
            </div>
        );
    }
});

var onChange = function () {
    ReactDOM.render(
        <Notepad notepad={notepad} onAddNote={onAddNote} onSelectNote={onSelectNote} onChangeNote={onChangeNote}/>,
        document.getElementById('container')
    );
};

onChange();

