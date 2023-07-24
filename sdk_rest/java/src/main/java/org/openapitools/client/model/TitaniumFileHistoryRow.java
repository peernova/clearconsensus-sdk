/*
 * clearconsensus-sdk
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import org.openapitools.client.model.TitaniumConsensusRunInfo;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonArray;
import com.google.gson.JsonDeserializationContext;
import com.google.gson.JsonDeserializer;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParseException;
import com.google.gson.TypeAdapterFactory;
import com.google.gson.reflect.TypeToken;

import java.lang.reflect.Type;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Set;

import org.openapitools.client.JSON;

/**
 * TitaniumFileHistoryRow
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-07-24T13:30:52.291583Z[UTC]")
public class TitaniumFileHistoryRow {
  public static final String SERIALIZED_NAME_CONSENSUS_RUN = "consensusRun";
  @SerializedName(SERIALIZED_NAME_CONSENSUS_RUN)
  private List<TitaniumConsensusRunInfo> consensusRun = null;

  public static final String SERIALIZED_NAME_LATEST_CONSENSUS_MEMBER = "latestConsensusMember";
  @SerializedName(SERIALIZED_NAME_LATEST_CONSENSUS_MEMBER)
  private Boolean latestConsensusMember;

  public static final String SERIALIZED_NAME_VALUES = "values";
  @SerializedName(SERIALIZED_NAME_VALUES)
  private List<Object> values = null;

  public TitaniumFileHistoryRow() { 
  }

  public TitaniumFileHistoryRow consensusRun(List<TitaniumConsensusRunInfo> consensusRun) {
    
    this.consensusRun = consensusRun;
    return this;
  }

  public TitaniumFileHistoryRow addConsensusRunItem(TitaniumConsensusRunInfo consensusRunItem) {
    if (this.consensusRun == null) {
      this.consensusRun = new ArrayList<>();
    }
    this.consensusRun.add(consensusRunItem);
    return this;
  }

   /**
   * Get consensusRun
   * @return consensusRun
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public List<TitaniumConsensusRunInfo> getConsensusRun() {
    return consensusRun;
  }


  public void setConsensusRun(List<TitaniumConsensusRunInfo> consensusRun) {
    this.consensusRun = consensusRun;
  }


  public TitaniumFileHistoryRow latestConsensusMember(Boolean latestConsensusMember) {
    
    this.latestConsensusMember = latestConsensusMember;
    return this;
  }

   /**
   * Get latestConsensusMember
   * @return latestConsensusMember
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Boolean getLatestConsensusMember() {
    return latestConsensusMember;
  }


  public void setLatestConsensusMember(Boolean latestConsensusMember) {
    this.latestConsensusMember = latestConsensusMember;
  }


  public TitaniumFileHistoryRow values(List<Object> values) {
    
    this.values = values;
    return this;
  }

  public TitaniumFileHistoryRow addValuesItem(Object valuesItem) {
    if (this.values == null) {
      this.values = new ArrayList<>();
    }
    this.values.add(valuesItem);
    return this;
  }

   /**
   * Get values
   * @return values
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public List<Object> getValues() {
    return values;
  }


  public void setValues(List<Object> values) {
    this.values = values;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TitaniumFileHistoryRow titaniumFileHistoryRow = (TitaniumFileHistoryRow) o;
    return Objects.equals(this.consensusRun, titaniumFileHistoryRow.consensusRun) &&
        Objects.equals(this.latestConsensusMember, titaniumFileHistoryRow.latestConsensusMember) &&
        Objects.equals(this.values, titaniumFileHistoryRow.values);
  }

  @Override
  public int hashCode() {
    return Objects.hash(consensusRun, latestConsensusMember, values);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TitaniumFileHistoryRow {\n");
    sb.append("    consensusRun: ").append(toIndentedString(consensusRun)).append("\n");
    sb.append("    latestConsensusMember: ").append(toIndentedString(latestConsensusMember)).append("\n");
    sb.append("    values: ").append(toIndentedString(values)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }


  public static HashSet<String> openapiFields;
  public static HashSet<String> openapiRequiredFields;

  static {
    // a set of all properties/fields (JSON key names)
    openapiFields = new HashSet<String>();
    openapiFields.add("consensusRun");
    openapiFields.add("latestConsensusMember");
    openapiFields.add("values");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Object and throws an exception if issues found
  *
  * @param jsonObj JSON Object
  * @throws IOException if the JSON Object is invalid with respect to TitaniumFileHistoryRow
  */
  public static void validateJsonObject(JsonObject jsonObj) throws IOException {
      if (jsonObj == null) {
        if (TitaniumFileHistoryRow.openapiRequiredFields.isEmpty()) {
          return;
        } else { // has required fields
          throw new IllegalArgumentException(String.format("The required field(s) %s in TitaniumFileHistoryRow is not found in the empty JSON string", TitaniumFileHistoryRow.openapiRequiredFields.toString()));
        }
      }

      Set<Entry<String, JsonElement>> entries = jsonObj.entrySet();
      // check to see if the JSON string contains additional fields
      for (Entry<String, JsonElement> entry : entries) {
        if (!TitaniumFileHistoryRow.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TitaniumFileHistoryRow` properties. JSON: %s", entry.getKey(), jsonObj.toString()));
        }
      }
      JsonArray jsonArrayconsensusRun = jsonObj.getAsJsonArray("consensusRun");
      if (jsonArrayconsensusRun != null) {
        // ensure the json data is an array
        if (!jsonObj.get("consensusRun").isJsonArray()) {
          throw new IllegalArgumentException(String.format("Expected the field `consensusRun` to be an array in the JSON string but got `%s`", jsonObj.get("consensusRun").toString()));
        }

        // validate the optional field `consensusRun` (array)
        for (int i = 0; i < jsonArrayconsensusRun.size(); i++) {
          TitaniumConsensusRunInfo.validateJsonObject(jsonArrayconsensusRun.get(i).getAsJsonObject());
        };
      }
      // ensure the json data is an array
      if (jsonObj.get("values") != null && !jsonObj.get("values").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `values` to be an array in the JSON string but got `%s`", jsonObj.get("values").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TitaniumFileHistoryRow.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TitaniumFileHistoryRow' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TitaniumFileHistoryRow> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TitaniumFileHistoryRow.class));

       return (TypeAdapter<T>) new TypeAdapter<TitaniumFileHistoryRow>() {
           @Override
           public void write(JsonWriter out, TitaniumFileHistoryRow value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TitaniumFileHistoryRow read(JsonReader in) throws IOException {
             JsonObject jsonObj = elementAdapter.read(in).getAsJsonObject();
             validateJsonObject(jsonObj);
             return thisAdapter.fromJsonTree(jsonObj);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of TitaniumFileHistoryRow given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of TitaniumFileHistoryRow
  * @throws IOException if the JSON string is invalid with respect to TitaniumFileHistoryRow
  */
  public static TitaniumFileHistoryRow fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TitaniumFileHistoryRow.class);
  }

 /**
  * Convert an instance of TitaniumFileHistoryRow to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

